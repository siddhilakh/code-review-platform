import uuid
from fastapi import APIRouter
from src.app.core.store import repositories, jobs

router = APIRouter(prefix="/repositories", tags=["repositories"])


@router.post("")
def add_repository(repo_url: str):
    repo = {"id": len(repositories) + 1, "url": repo_url}
    repositories.append(repo)
    return repo


@router.get("")
def list_repositories():
    return repositories


@router.get("/{repo_id}")
def get_repository(repo_id: int):
    for repo in repositories:
        if repo["id"] == repo_id:
            return repo
    return {"error": "not found"}


@router.post("/{repo_id}/analyze")
def analyze_repository(repo_id: int):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"status": "queued", "progress": 0, "repo_id": repo_id}
    return {"job_id": job_id, "status": "queued"}