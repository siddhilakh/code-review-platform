from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.app.core.database import get_db
from src.app import models, schemas

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("/{job_id}", response_model=schemas.JobOut)
def get_job_status(job_id: str, db: Session = Depends(get_db)):
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return job