from fastapi import APIRouter, Depends
from sqlmodel import Session
from db.db import get_session

from models.genre_model import Genre

from repository.genres_repository import *


router = APIRouter()

@router.get("/api/genres")
def get_genres(session: Session = Depends(get_session)):
    return get_all(session)

@router.put("/api/genres/{genre_id}")
def update_genre(genre_id: int, updated_genre: Genre, session: Session = Depends(get_session)):
    genre = get_by_id(genre_id, session)
    if genre:
        return put_genre(genre, updated_genre, session)
    return {"error": "Genre not found", "status_code": 404}