import os
import sqlite3
from pathlib import Path
from typing import List, Any
from datetime import datetime


# IMPORT GENERATORS
from generators import (
    generate_organizations,
    generate_teams,
    generate_users,
    generate_team_memberships,
    generate_projects,
    generate_sections,
    generate_tasks,
    generate_subtasks,
    generate_comments,
    generate_custom_field_definitions,
    generate_custom_field_values,
    generate_tags,
    generate_task_tags,
    generate_task_dependencies,
)

# CONFIGURATION
BASE_DIR = Path(__file__).resolve().parent.parent
SCHEMA_PATH = BASE_DIR / "schema.sql"
OUTPUT_DIR = BASE_DIR / "output"
DB_PATH = OUTPUT_DIR / "asana_simulation.sqlite"

# Ensure output directory exists
OUTPUT_DIR.mkdir(exist_ok=True)



# DATABASE HELPERS
def connect_db(db_path: Path) -> sqlite3.Connection:
    """
    Create SQLite connection with foreign keys enabled.
    """
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def execute_schema(conn: sqlite3.Connection, schema_path: Path):
    """
    Execute schema.sql to create all tables.
    """
    with open(schema_path, "r", encoding="utf-8") as f:
        sql = f.read()
    conn.executescript(sql)
    conn.commit()


def insert_many(
    conn: sqlite3.Connection,
    table: str,
    columns: List[str],
    rows: List[Any]
):
    """
    Generic bulk insert utility.
    """
    if not rows:
        return

    placeholders = ", ".join(["?"] * len(columns))
    col_str = ", ".join(columns)
    query = f"INSERT INTO {table} ({col_str}) VALUES ({placeholders})"

    values = [
        tuple(getattr(row, col) for col in columns)
        for row in rows
    ]

    conn.executemany(query, values)
    conn.commit()



# MAIN ORCHESTRATION
def main():
    print(" Starting Asana Seed Data Generation")

   
    # 1. INIT DATABASE
   
    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = connect_db(DB_PATH)
    execute_schema(conn, SCHEMA_PATH)

    
    # 2. GENERATE DATA (ORDER MATTERS)
    

    #Organizations
    organizations = generate_organizations()
    org = organizations[0]

    insert_many(
        conn,
        "organizations",
        ["org_id", "name", "mail", "created_at"],
        organizations
    )

    #Teams
    teams = generate_teams(org.org_id)
    insert_many(
        conn,
        "teams",
        ["team_id", "org_id", "name", "description", "created_at"],
        teams
    )

    #Users
    users = generate_users(org.org_id, count=2500)
    insert_many(
        conn,
        "users",
        ["user_id", "org_id", "name", "email", "role", "job_title", "created_at", "is_active"],
        users
    )

    #Team Memberships
    team_memberships = generate_team_memberships(users, teams)
    insert_many(
        conn,
        "team_memberships",
        ["user_id", "team_id", "joined_at", "is_admin"],
        team_memberships
    )

    #Projects
    projects = generate_projects(org.org_id, teams)
    insert_many(
        conn,
        "projects",
        ["project_id", "team_id", "org_id", "name", "description",
         "status", "start_date", "end_date", "created_at"],
        projects
    )

    #Sections
    sections = generate_sections(projects)
    insert_many(
        conn,
        "sections",
        ["section_id", "project_id", "name", "position"],
        sections
    )

    #Tasks
    tasks = generate_tasks(projects, sections, users)
    insert_many(
        conn,
        "tasks",
        ["task_id", "project_id", "section_id", "assignee_id",
         "name", "description", "due_date", "priority",
         "completed", "created_at", "completed_at"],
        tasks
    )

    #Subtasks
    subtasks = generate_subtasks(tasks)
    insert_many(
        conn,
        "subtasks",
        ["subtask_id", "parent_task_id", "assignee_id",
         "name", "completed", "created_at", "completed_at"],
        subtasks
    )

    #Comments
    comments = generate_comments(tasks, users)
    insert_many(
        conn,
        "comments",
        ["comment_id", "task_id", "user_id", "type", "content", "created_at"],
        comments
    )

    #Custom Field Definitions
    custom_field_defs = generate_custom_field_definitions(projects)
    insert_many(
        conn,
        "custom_field_definitions",
        ["field_id", "project_id", "name", "field_type", "created_at"],
        custom_field_defs
    )

    #Custom Field Values
    custom_field_values = generate_custom_field_values(tasks, custom_field_defs)
    insert_many(
        conn,
        "custom_field_values",
        ["task_id", "field_id", "value"],
        custom_field_values
    )

    #Tags
    tags = generate_tags()
    insert_many(
        conn,
        "tags",
        ["tag_id", "name", "created_at"],
        tags
    )

    #Task–Tag Associations
    task_tags = generate_task_tags(tasks, tags)
    insert_many(
        conn,
        "task_tags",
        ["task_id", "tag_id"],
        task_tags
    )

    #Task Dependencies
    task_dependencies = generate_task_dependencies(tasks)
    insert_many(
        conn,
        "task_dependencies",
        ["dependency_id", "blocking_task_id", "blocked_task_id", "created_at"],
        task_dependencies
    )

   
    # 3. FINALIZE
    conn.close()

    print(" Database generated successfully")
    print(f" Location: {DB_PATH}")
    print(" Ready for RL / analysis / inspection")



# ENTRY POINT
if __name__ == "__main__":
    main()
