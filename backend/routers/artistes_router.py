from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from db.db import get_session

from models.artist_model import Artist

from repository.artistes_repository import *
from repository.albums_repository import del_albums_with_artist

from auth import get_current_user

router = APIRouter()

@router.get("/api/artists")
def get_artists(session: Session = Depends(get_session)):
    return get_all(session)

@router.get("/api/artists/{artist_id}")
def get_artist(artist_id: int, session: Session = Depends(get_session)):
    artist = get_by_id(session, artist_id)
    if artist:
        return artist
    return {
            "error": "Artist not found",
            "status_code": 404
            }


@router.get("/api/artists/{artist_id}/songs")
def get_artist_songs(artist_id: int, session: Session = Depends(get_session)):
    artist = get_by_id(session, artist_id)
    if artist is None:
        return {
            "error": "Artist not found",
            "status_code": 404
        }
    
    musics = get_musics_by_artist(session, artist_id)
    return musics

@router.put("/api/artists/{artist_id}")
def update_artist(artist_id: int, updated_artist: Artist, session: Session = Depends(get_session)):
    artist = get_by_id(session, artist_id)
    if artist:
        return put_artist(session, artist, updated_artist)
    return {"error": "Artist not found", "status_code": 404}

@router.delete("/api/artists/{artist_id}")
def delete_artist(artist_id: int, session: Session = Depends(get_session), current_user: int =Depends(get_current_user)):
    artist = get_by_id(session, artist_id)
    if artist:
        del_albums_with_artist(session, artist)
        del_artist(session, artist)
        return {"message": "Artist deleted successfully"}
    return {"error": "Artist not found", "status_code": 404}