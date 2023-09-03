from fastapi import Depends
from app.core.database import Session

def get_session() -> Session:
    return Session()