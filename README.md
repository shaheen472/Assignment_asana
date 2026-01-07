# Asana Seed Data Simulation for RL Environments

## Overview

This repository implements a **realistic, enterprise-grade seed data generator** that simulates an **Asana workspace** for a large B2B SaaS company.  
The generated data is designed to serve as **high-quality seed data** for **Reinforcement Learning (RL) environments** that evaluate AI agents performing project-management workflows.

The simulation closely mirrors **real Asana usage patterns**, avoiding unrealistic shortcuts such as uniform distributions, trivial task names, or flat timelines.

**Target organization:**  
- Company: **Veeva Systems**  
- Industry: Enterprise B2B SaaS  
- Size: 5,000–10,000 employees  

---

## Key Objectives

- Create a **fully relational SQLite database** representing an Asana workspace
- Maintain **temporal, relational, and behavioral realism**
- Follow **research-backed distributions** for tasks, projects, users, and workflows
- Ensure the dataset is suitable for **RL training, evaluation, and fine-tuning**

## Repository Structure
├── README.md # Project documentation
├── requirements.txt # Python dependencies
├── schema.sql # SQLite schema (DDL)
├── .env.example # Environment variable template
├── src/
│ ├── main.py # Entry point / orchestration
│ ├── models/ # Data models (row-level contracts)
│ ├── utils/ # Shared intelligence (UUIDs, dates, distributions)
│ ├── scrapers/ # Curated real-world reference data
│ └── generators/ # Seed data generators (core logic)
└── output/
└── asana_simulation.sqlite # Final generated database

## Database Schema (Section A)

The schema is defined in `schema.sql` and includes **14 tables**:

1. Organizations / Workspaces  
2. Teams  
3. Users  
4. Team Memberships  
5. Projects  
6. Sections  
7. Tasks  
8. Subtasks  
9. Comments (Stories)  
10. Custom Field Definitions  
11. Custom Field Values  
12. Tags  
13. Task–Tag Associations  
14. Task Dependencies  

Key design principles:
- UUIDs simulate Asana Global IDs (GIDs)
- Foreign keys enforce referential integrity
- Composite primary keys used for join tables
- Temporal consistency enforced across entities

---

## Seed Data Methodology (Section B)

The seed data is generated using **explicit, column-level strategies**, including:

- **Scraped / Curated Data**
  - Organization name, domain, team structures, role hierarchies
- **Synthetic Data with Research-Based Distributions**
  - Task completion rates
  - Due-date horizons
  - User activity status
- **Heuristics**
  - Workload balancing
  - Assignment probabilities
  - Admin ratios in teams
- **Temporal Consistency**
  - `completed_at` always after `created_at`
  - Dependencies created only after both tasks exist
- **Relational Consistency**
  - Tasks belong to correct projects and sections
  - Dependencies restricted within projects

---

## Architecture Overview

### `models/`
Defines **what valid data looks like**.  
Each file represents one table and acts as a **contract** for generators.

### `utils/`
Centralized shared logic:
- UUID generation
- Date and timestamp distributions
- Probability samplers
- Workload balancing
- Validation helpers
- Optional LLM wrappers

This prevents duplicated logic and realism bugs.

### `scrapers/`
Curated real-world references:
- Organization details (Veeva Systems)
- Team catalogs
- Project name templates
- Role hierarchies
- Name corpora

No live web scraping is used to ensure reproducibility.

### `generators/`
Implements **Section B methodology**.
Each generator:
- Produces structured model objects
- Applies realistic distributions
- Does NOT insert into the database
- Does NOT depend on execution order

### `main.py`
The **single entry point** that:
1. Initializes the SQLite database
2. Executes `schema.sql`
3. Runs generators in dependency order
4. Inserts data safely
5. Produces the final database

---

## Execution Order (Critical)
├── README.md # Project documentation
├── requirements.txt # Python dependencies
├── schema.sql # SQLite schema (DDL)
├── .env.example # Environment variable template
├── src/
│ ├── main.py # Entry point / orchestration
│ ├── models/ # Data models (row-level contracts)
│ ├── utils/ # Shared intelligence (UUIDs, dates, distributions)
│ ├── scrapers/ # Real-world reference data (curated)
│ └── generators/ # Seed data generators (core logic)
└── output/
└── asana_simulation.sqlite # Final generated database

The generators are executed in the following order to ensure integrity:

1. Organizations  
2. Teams  
3. Users  
4. Team Memberships  
5. Projects  
6. Sections  
7. Tasks  
8. Subtasks  
9. Comments  
10. Custom Field Definitions  
11. Custom Field Values  
12. Tags  
13. Task–Tag Associations  
14. Task Dependencies  

This guarantees that no record references a non-existent parent.

---

## How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt

Output-
A fully populated SQLite database will be created at:

output/asana_simulation.sqlite


