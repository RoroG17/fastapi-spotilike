from fastapi import APIRouter, Depends
from sqlmodel import Session
from db.db import get_session

from models.album_model import Album
from models.music_model import Music

from repository.albums_repository import *
from repository.artistes_repository import get_by_id as get_artist_by_id
from repository.genres_repository import get_by_id as get_genre_by_id

from auth import get_current_user

from datetime import date, time


router = APIRouter()

@router.get("/api/albums")
def get_albums(session: Session = Depends(get_session)):
   return get_all(session)

@router.get("/api/albums/{album_id}")
def get_album(album_id: int, session: Session = Depends(get_session)):
    result = get_by_id(session, album_id)
    if result:
        return result
    return {
            "error": "Album not found",
            "status_code": 404
            }

@router.get("/api/albums/{album_id}/songs")
def get_album_songs(album_id: int, session: Session = Depends(get_session)):
    if get_by_id(session, album_id) is None:
        return {
            "error": "Album not found",
            "status_code": 404
        }
    
    musics = get_musics_by_album(session, album_id)
    if musics:
        return musics
    return {
        "message": "No songs found for this album",
        "status_code": 400
    }

@router.post("/api/albums")
def create_album(album: Album, session: Session = Depends(get_session)): 
    if isinstance(album.release_year, str):
        album.release_year = date.fromisoformat(album.release_year)
    if get_artist_by_id(session, album.artist_id) is None:
        return {
            "error": "Artist not found",
            "status_code": 404
        }
    return post_album(session, album)

@router.post("/api/albums/{album_id}/songs")
def add_song_to_album(album_id: int, music: Music, session: Session = Depends(get_session)):
    album = session.get(Album, album_id)
    if album:
        if isinstance(music.duration, str):
            music.duration = time.fromisoformat(music.duration)
            if get_genre_by_id(music.genre_id, session) is None:
                return {
                    "error": "Genre not found",
                    "status_code": 404
                }
            if get_artist_by_id(session, music.artist_id) is None:
                return {
                    "error": "Artist not found",
                    "status_code": 404
                }
            if get_by_id(session, music.album_id) is None:
                return {
                    "error": "Album not found",
                    "status_code": 404
                }
        return add_music_to_album(session, album, music)
    return {"error": "Album not found", "status_code": 404}

@router.put("/api/albums/{album_id}")
def update_album(album_id: int, updated_album: Album, session: Session = Depends(get_session)):
    album = session.get(Album, album_id)
    if album:
        if isinstance(updated_album.release_year, str):
            updated_album.release_year = date.fromisoformat(updated_album.release_year)
        return put_album(session, album, updated_album)
    return {"error": "Album not found", "status_code": 404}

@router.delete("/api/albums/{album_id}")
def delete_album(album_id: int, session: Session = Depends(get_session), current_user: int =Depends(get_current_user)):
    album = session.get(Album, album_id)
    if album:
        del_album(session, album)
        return {"message": "Album deleted successfully", "status_code": 200}
    return {"error": "Album not found", "status_code": 404}