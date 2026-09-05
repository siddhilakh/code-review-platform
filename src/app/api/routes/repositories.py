import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.app.core.database import get_db
from src.app import models, schemas

router = APIRouter(prefix="/repositories", tags=["repositories"])


@router.post("", response_model=schemas.RepositoryOut)
def add_repository(payload: schemas.RepositoryCreate, db: Session = Depends(get_db)):
    repo = models.Repository(url=payload.url)
    db.add(repo)
    db.commit()
    db.refresh(repo)  # pulls back the generated id and created_at
    return repo


@router.get("", response_model=list[schemas.RepositoryOut])
def list_repositories(db: Session = Depends(get_db)):
    return db.query(models.Repository).all()


@router.get("/{repo_id}", response_model=schemas.RepositoryOut)
def get_repository(repo_id: int, db: Session = Depends(get_db)):
    repo = db.query(models.Repository).filter(models.Repository.id == repo_id).first()
    if repo is None:
        raise HTTPException(status_code=404, detail="Repository not found")
    return repo


@router.post("/{repo_id}/analyze", response_model=schemas.JobOut)
def analyze_repository(repo_id: int, db: Session = Depends(get_db)):
    repo = db.query(models.Repository).filter(models.Repository.id == repo_id).first()
    if repo is None:
        raise HTTPException(status_code=404, detail="Repository not found")

    job = models.Job(id=str(uuid.uuid4()), status="queued", progress=0, repository_id=repo_id)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job