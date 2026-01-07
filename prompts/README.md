# Prompt Templates

This directory contains **LLM prompt templates** used for generating
realistic text content in the Asana seed data simulation.

## Why Prompts Are Externalized

- To make prompt engineering **transparent and auditable**
- To avoid hiding realism logic inside Python code
- To allow easy iteration without code changes

## Usage

These prompts are consumed by optional LLM wrappers
(`utils/llm_utils.py`) and parameterized at runtime with:
- Project context
- Team function
- Task type
- Workflow stage

If no LLM API key is provided, the system falls back to
template-based placeholder text.

## Prompt Files

- `task_name.prompt` — Task titles
- `task_description.prompt` — Task descriptions
- `comment.prompt` — Human & system comments
- `project_description.prompt` — Project-level summaries
