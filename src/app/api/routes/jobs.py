from fastapi import APIRouter
from src.app.core.store import jobs

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("/{job_id}")
def get_job_status(job_id: str):
    job = jobs.get(job_id)
    if job is None:
        return {"error": "not found"}
    return job