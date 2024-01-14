from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()from fastapi import Depends
from app.core.database import Session

def get_session() -> Session:
    return Session()