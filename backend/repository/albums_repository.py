from sqlmodel import Session, select

from models.artist_model import Artist
from models.album_model import Album
from models.music_model import Music
from models.genre_model import Genre

def get_all(session: Session):
    albums = session.exec(select(Album)).all()
    return albums

def get_by_id(session: Session, album_id: int):
    statement = (
        select(Album, Artist)
        .join(Artist, Album.artist_id == Artist.id)
        .where(Album.id == album_id)
    )
    result = session.execute(statement).first()
    if not result:
        return None

    album, artist = result
    return {
        "album_id": album.id,
        "title": album.title,
        "release_year": album.release_year,
        "cover": album.cover,
        "artist_id": artist.id,
        "artist_name": artist.name,
    } 

def get_musics_by_album(session: Session, album_id: int):
    statement = (
        select(Music, Genre)
        .join(Genre, Music.genre_id == Genre.id)
        .where(Music.album_id == album_id)
    )
    album = session.exec(statement).all()
    if album:
        return [{
            "id": music.id,
            "title": music.title,
            "duration": music.duration,
            "genre_id": genre.id,
            "genre": genre.name,
            "album_id": music.album_id,
            "artist_id": music.artist_id
        } for music, genre in album]
    return []

def post_album(session: Session, album: Album):
    session.add(album)
    session.commit()
    session.refresh(album)
    return album

def add_music_to_album(session: Session, album: Album, music: Music):
    music.album_id = album.id
    session.add(music)
    session.commit()
    session.refresh(music)
    return music

def put_album(session: Session, album: Album, updated_album: Album):
    album.title = updated_album.title
    album.release_year = updated_album.release_year
    album.cover = updated_album.cover
    album.artist_id = updated_album.artist_id
    session.add(album)
    session.commit()
    session.refresh(album)
    return album   

def del_album(session: Session, album: Album):
    session.delete(album)
    session.commit()

def del_albums_with_artist(session: Session, artist: Artist):
    albums = session.exec(select(Album).where(Album.artist_id == artist.id)).all()
    for album in albums:
        session.delete(album)
    session.commit()