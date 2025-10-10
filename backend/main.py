# app/main.py
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from auth import create_access_token, get_current_user

from db.db import get_session
from models.artist_model import Artist
from models.music_model import Music
from models.album_model import Album
from models.genre_model import Genre
from models.user_model import User
from models.auth_model import Token

from datetime import date, time

app = FastAPI()

@app.get("/api/albums")
def get_albums(session: Session = Depends(get_session)):
    albums = session.exec(select(Album)).all()
    return albums

@app.get("/api/albums/{album_id}")
def get_album(album_id: int, session: Session = Depends(get_session)):
    album = session.get(Album, album_id)
    return album

@app.get("/api/albums/{album_id}/songs")
def get_album_songs(album_id: int, session: Session = Depends(get_session)):
    album = session.get(Album, album_id)
    if album:
        return album.musics
    return []

@app.get("/api/genres")
def get_genres(session: Session = Depends(get_session)):
    genres = session.exec(select(Genre)).all()
    return genres

@app.get("/api/artists/{artist_id}/songs")
def get_artist_songs(artist_id: int, session: Session = Depends(get_session)):
    artist = session.get(Artist, artist_id)
    if artist:
        return artist.musics
    return []

@app.post("/api/users/signup")
def signup_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@app.post("/api/users/login", response_model=Token)
def login_user(user_credentials : OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.username == user_credentials.username)).first()
    if user and user.hashed_password == user_credentials.password:
        token = create_access_token(data={"user_id": user.id})
        return {"message": "Login successful", "access_token": token, "token_type": "bearer"}
    return {"error": "Invalid credentials"}

@app.post("/api/albums")
def create_album(album: Album, session: Session = Depends(get_session)): 
    if isinstance(album.release_year, str):
        album.release_year = date.fromisoformat(album.release_year)

    session.add(album)
    session.commit()
    session.refresh(album)
    return album

@app.post("/api/albums/{album_id}/songs")
def add_song_to_album(album_id: int, music: Music, session: Session = Depends(get_session)):
    album = session.get(Album, album_id)
    if album:
        if isinstance(music.duration, str):
            music.duration = time.fromisoformat(music.duration)
        music.album_id = album_id
        session.add(music)
        session.commit()
        session.refresh(music)
        return music
    return {"error": "Album not found"}

@app.put("/api/artists/{artist_id}")
def update_artist(artist_id: int, updated_artist: Artist, session: Session = Depends(get_session)):
    artist = session.get(Artist, artist_id)
    if artist:
        artist.name = updated_artist.name
        artist.avatar = updated_artist.avatar
        artist.bio = updated_artist.bio
        session.add(artist)
        session.commit()
        session.refresh(artist)
        return artist
    return {"error": "Artist not found"}

@app.put("/api/albums/{album_id}")
def update_album(album_id: int, updated_album: Album, session: Session = Depends(get_session)):
    album = session.get(Album, album_id)
    if album:
        if isinstance(updated_album.release_year, str):
            updated_album.release_year = date.fromisoformat(updated_album.release_year)
        album.title = updated_album.title
        album.cover = updated_album.cover
        album.release_year = updated_album.release_year
        album.artist_id = updated_album.artist_id
        session.add(album)
        session.commit()
        session.refresh(album)
        return album
    return {"error": "Album not found"}

@app.put("/api/genres/{genre_id}")
def update_genre(genre_id: int, updated_genre: Genre, session: Session = Depends(get_session)):
    genre = session.get(Genre, genre_id)
    if genre:
        genre.name = updated_genre.name
        genre.description = updated_genre.description
        session.add(genre)
        session.commit()
        session.refresh(genre)
        return genre
    return {"error": "Genre not found"}

@app.delete("/api/users/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_session), current_user: int =Depends(get_current_user)):
    print(current_user)
    user = session.get(User, user_id)
    if user:
        session.delete(user)
        session.commit()
        return {"message": "User deleted successfully"}
    return {"error": "User not found"}

@app.delete("/api/albums/{album_id}")
def delete_album(album_id: int, session: Session = Depends(get_session), current_user: int =Depends(get_current_user)):
    print(current_user)
    album = session.get(Album, album_id)
    if album:
        session.delete(album)
        session.commit()
        return {"message": "Album deleted successfully"}
    return {"error": "Album not found"}

@app.delete("/api/artists/{artist_id}")
def delete_artist(artist_id: int, session: Session = Depends(get_session), current_user: int =Depends(get_current_user)):
    print(current_user)
    artist = session.get(Artist, artist_id)
    if artist:
        session.delete(artist)
        session.commit()
        return {"message": "Artist deleted successfully"}
    return {"error": "Artist not found"}
