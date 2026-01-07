PRAGMA foreign_keys = ON;

-- 1. Organizations / Workspaces
CREATE TABLE organizations (
    org_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    mail TEXT,
    created_at TIMESTAMP
);

-- 2. Teams
CREATE TABLE teams (
    team_id TEXT PRIMARY KEY,
    org_id TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (org_id) REFERENCES organizations(org_id)
);

-- 3. Users
CREATE TABLE users (
    user_id TEXT PRIMARY KEY,
    org_id TEXT NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    role TEXT,
    job_title TEXT,
    created_at TIMESTAMP,
    is_active BOOLEAN,
    FOREIGN KEY (org_id) REFERENCES organizations(org_id),
    UNIQUE (org_id, email)
);

-- 4. Team Memberships
CREATE TABLE team_memberships (
    user_id TEXT NOT NULL,
    team_id TEXT NOT NULL,
    joined_at TIMESTAMP,
    is_admin BOOLEAN,
    PRIMARY KEY (user_id, team_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

-- 5. Projects
CREATE TABLE projects (
    project_id TEXT PRIMARY KEY,
    team_id TEXT NOT NULL,
    org_id TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    status TEXT,
    start_date DATE,
    end_date DATE,
    created_at TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(team_id),
    FOREIGN KEY (org_id) REFERENCES organizations(org_id)
);

-- 6. Sections
CREATE TABLE sections (
    section_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    name TEXT NOT NULL,
    position INTEGER,
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- 7. Tasks
CREATE TABLE tasks (
    task_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    section_id TEXT,
    assignee_id TEXT,
    name TEXT NOT NULL,
    description TEXT,
    due_date TEXT,
    priority TEXT,
    completed BOOLEAN,
    created_at TIMESTAMP,
    completed_at TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id),
    FOREIGN KEY (section_id) REFERENCES sections(section_id),
    FOREIGN KEY (assignee_id) REFERENCES users(user_id)
);

-- 8. Subtasks
CREATE TABLE subtasks (
    subtask_id TEXT PRIMARY KEY,
    parent_task_id TEXT NOT NULL,
    assignee_id TEXT,
    name TEXT NOT NULL,
    completed BOOLEAN,
    created_at TIMESTAMP,
    completed_at TIMESTAMP,
    FOREIGN KEY (parent_task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (assignee_id) REFERENCES users(user_id)
);

-- 9. Comments
CREATE TABLE comments (
    comment_id TEXT PRIMARY KEY,
    task_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    type TEXT,
    content TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- 10. Custom Field Definitions
CREATE TABLE custom_field_definitions (
    field_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    name TEXT NOT NULL,
    field_type TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- 11. Custom Field Values
CREATE TABLE custom_field_values (
    task_id TEXT NOT NULL,
    field_id TEXT NOT NULL,
    value TEXT,
    PRIMARY KEY (task_id, field_id),
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (field_id) REFERENCES custom_field_definitions(field_id)
);

-- 12. Tags
CREATE TABLE tags (
    tag_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    created_at TIMESTAMP
);

-- 13. Task-Tag Associations
CREATE TABLE task_tags (
    task_id TEXT NOT NULL,
    tag_id TEXT NOT NULL,
    PRIMARY KEY (task_id, tag_id),
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id)
);

-- 14. Task Dependencies
CREATE TABLE task_dependencies (
    dependency_id TEXT PRIMARY KEY,
    blocking_task_id TEXT NOT NULL,
    blocked_task_id TEXT NOT NULL,
    created_at TIMESTAMP,
    FOREIGN KEY (blocking_task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (blocked_task_id) REFERENCES tasks(task_id)
);
