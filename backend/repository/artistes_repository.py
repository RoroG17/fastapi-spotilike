from sqlmodel import Session, select
from models.artist_model import Artist

from models.music_model import Music
from models.genre_model import Genre

def get_all(session: Session):
    artistes = session.exec(select(Artist)).all()
    return artistes

def get_by_id(session: Session, artist_id: int):
    artist = session.get(Artist, artist_id)
    return artist

def get_musics_by_artist(session: Session, artist_id: int):
    statement = (
        select(Music, Genre)
        .join(Genre, Music.genre_id == Genre.id)
        .where(Music.artist_id == artist_id)
    )
    musics = session.exec(statement).all()

    if musics:
        return [{
            "id": music.id,
            "title": music.title,
            "duration": music.duration,
            "genre_id": genre.id,
            "genre": genre.name,
            "album_id": music.album_id,
            "artist_id": music.artist_id
        } for music, genre in musics]
    return []

def put_artist(session: Session, artist: Artist, updated_artist: Artist):
    artist.name = updated_artist.name
    artist.avatar = updated_artist.avatar
    artist.bio = updated_artist.bio
    session.add(artist)
    session.commit()
    session.refresh(artist)
    return artist

def del_artist(session: Session, artist: Artist):
    session.delete(artist)
    session.commit()