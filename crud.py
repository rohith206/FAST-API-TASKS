from sqlalchemy.orm import Session
from . import models, schemas


# Create
def create_task(db: Session, task: schemas.TaskCreate) -> models.Task:
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


# Read single
def get_task(db: Session, task_id: int) -> models.Task | None:
    return db.query(models.Task).filter(models.Task.id == task_id).first()


# Read multiple with optional search
def get_tasks(db: Session, skip: int = 0, limit: int = 100, q: str | None = None):
    query = db.query(models.Task)
    if q:
# simple case-insensitive search on title and description
        likeq = f"%{q}%"
    query = query.filter((models.Task.title.ilike(likeq)) | (models.Task.description.ilike(likeq)))
    return query.offset(skip).limit(limit).all()


# Update
def update_task(db: Session, task: models.Task, updates: schemas.TaskUpdate) -> models.Task:
    data = updates.dict(exclude_unset=True)
    for key, value in data.items():
        setattr(task, key, value)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


# Delete
def delete_task(db: Session, task: models.Task):
    db.delete(task)
    db.commit()