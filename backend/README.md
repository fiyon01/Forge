 # Forge Backend

Backend service for Forge.

## Requirements

- Python 3.11 or newer
- [uv](https://docs.astral.sh/uv/) for Python and dependency management
- Any project services required by the application (for example, a database or cache)

Check the project's `pyproject.toml` for the exact supported Python version and configured services.

## Installation

From this directory, install uv if it is not already available:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart your shell if necessary, then install the project dependencies:

```bash
uv sync
```

`uv sync` creates or updates the local virtual environment and installs the locked dependencies. Use the repository's lock file as committed; do not remove it unless dependencies are intentionally being updated.

## Configuration

Create a local environment file when the project provides an example:

```bash
cp .env.example .env
```

Update `.env` with local values such as database URLs, secret keys, and service credentials. Never commit secrets or production credentials. If no `.env.example` exists, inspect the application settings module and `pyproject.toml` for required variables.

Start any required external services before launching the backend. Use the project's Docker Compose configuration, if provided:

```bash
docker compose up -d
```

## Running the backend

Run commands through uv so they use the project environment:

```bash
uv run <application-command>
```

For an ASGI application, the development command is typically:

```bash
uv run uvicorn <module>:<app> --reload
```

Replace `<module>:<app>` with the import path defined by this project (for example, `app.main:app`). The API will normally be available at `http://127.0.0.1:8000`.

## Database migrations

If database migrations are configured, apply them before starting the application. For Alembic projects, this is commonly:

```bash
uv run alembic upgrade head
```

Use the migration tool and commands defined by the project rather than modifying the database schema manually.

## Tests and quality checks

Run the available checks from the backend directory:

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

If a command is not configured in `pyproject.toml`, omit it or use the project's configured equivalent.

## Updating dependencies

Add or remove dependencies with uv so both the project metadata and lock file stay synchronized:

```bash
uv add <package>
uv remove <package>
uv lock
uv sync
```

## Troubleshooting

- Run commands from `/backend`, where `pyproject.toml` is located.
- Run `uv sync` after changing dependencies or switching branches.
- Verify that required environment variables and external services are available.
- Use `uv run python --version` and `uv run pip list` to inspect the active environment.
