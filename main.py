from fastapi import FastAPI, HTTPException, Query, Path, Depends
from DB import models
from DB.models import Todos
from starlette import status
from pydantic import BaseModel, Field
from DB.database import SessionLocal, engine
from typing import Annotated
from sqlalchemy.orm import Session

# dependency injection

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

##API endpoint


@app.get("/", status_code=status.HTTP_200_OK)
def read_records(db: db_dependency, todo_id: int = Query(gt=0)):
    return db.query().all()


@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
def read_records(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(todo_id).all()
    if todo_model is not None:
        return todo_model
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Record is not found for ID"
    )


class TodoRequest(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    description: str = Field(min_length=2, max_length=100)
    priority: int = Field(default=5, gt=0, lt=6)
    complete: bool = False


@app.post("/todo", status_code=status.HTTP_201_CREATED)
def create_todo_item(db: db_dependency, new_todo_request: TodoRequest):
    new_todo = Todos(**new_todo_request.model_dump())
    db.add(new_todo)
    db.commit()
