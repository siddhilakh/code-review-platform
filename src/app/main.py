from fastapi import FastAPI

app = FastAPI(title="Code Review & Repository Analysis Platform")


@app.get("/health")
def health():
    """Liveness check — is the process running at all?"""
    return {"status": "ok"}


@app.get("/ready")
def ready():
    """Readiness check — is the app ready to serve real traffic?
    Right now this is the same as /health, but once we add a database
    and Redis connection (later phases), this is where we'll actually
    check those dependencies are reachable before saying 'ready'.
    """
    return {"status": "ok"}