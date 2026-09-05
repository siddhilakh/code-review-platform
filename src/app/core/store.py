# Temporary in-memory state shared across routers.
# Replaced entirely by PostgreSQL in Phase 2 — nothing here survives a restart.
repositories: list[dict] = []
jobs: dict[str, dict] = {}