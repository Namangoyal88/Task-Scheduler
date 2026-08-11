# Task-Scheduler (Planner AI)

An AI-powered goal planning system that breaks down a high-level goal into a structured, time-bound task plan. Given a goal, a timeframe, and a granularity, it generates an actionable schedule — accessible via a REST API, a CLI, and a UI.

## Features

- **Goal-to-plan generation** — Converts a natural-language goal into a structured task plan.
- **Configurable timeframe** — Plan across a `MONTHLY` or `YEARLY` horizon.
- **Configurable granularity** — Break the plan down by `DAILY`, `WEEKLY`, or `MONTHLY` tasks.
- **Optional start date** — Anchor the generated plan to a specific start date.
- **Multiple interfaces**:
  - REST API (FastAPI)
  - Command-line interface (CLI)
  - UI (`ui.py`)
- **Evaluation script** — Includes `evaluate.py` for assessing plan quality/output.

## Tech Stack

- Python
- FastAPI
- Pydantic
- argparse (CLI)

## Project Structure

```
Task-Scheduler/
├── app.py              # FastAPI application exposing the /generate endpoint
├── cli.py              # Command-line interface for plan generation
├── ui.py                # UI for interacting with the planner
├── evaluate.py          # Evaluation script for generated plans
├── planner/
│   └── planner.py        # Core GoalPlanner logic
├── outputs/              # Generated plan outputs
├── tests/                # Test suite
└── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.10+

### Installation

```bash
git clone https://github.com/Namangoyal88/Task-Scheduler.git
cd Task-Scheduler
pip install -r requirements.txt
```

## Usage

### REST API

Start the server:

```bash
uvicorn app:app --reload
```

**`GET /`** — Health check, confirms the API is running.

**`POST /generate`** — Generate a plan.

```json
{
  "goal": "Learn machine learning",
  "timeframe": "MONTHLY",
  "granularity": "WEEKLY",
  "startDate": "2026-09-01"
}
```

- `goal` (required) — The objective to plan for.
- `timeframe` (required) — `MONTHLY` or `YEARLY`.
- `granularity` (required) — `DAILY`, `WEEKLY`, or `MONTHLY`.
- `startDate` (optional) — ISO date (`YYYY-MM-DD`) to anchor the plan.

### CLI

```bash
python cli.py --goal "Learn machine learning" --timeframe MONTHLY --granularity WEEKLY --start-date 2026-09-01
```

Outputs the generated plan as formatted JSON.

### UI

```bash
python ui.py
```

## How It Works

1. A goal, timeframe, and granularity are submitted via the API, CLI, or UI.
2. The `GoalPlanner` (in `planner/planner.py`) processes the request and generates a structured task breakdown matching the requested time horizon and granularity.
3. The resulting plan is returned as JSON (API/CLI) or rendered in the UI.

## License

This project currently has no license specified.