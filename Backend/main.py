from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, User as UserSchema
from crud import get_user, create_user
from database import SessionLocal, engine

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=UserSchema)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, username=user.username, email=user.email)
    return db_user

@app.get("/users/{user_id}", response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user