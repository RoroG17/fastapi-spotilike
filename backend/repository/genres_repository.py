from sqlmodel import Session, select
from models.genre_model import Genre

def get_all(session: Session):
        genres = session.exec(select(Genre)).all()
        return genres

def get_by_id(genre_id: int, session: Session):
        genre = session.get(Genre, genre_id)
        return genre

def put_genre(genre: Genre, updated_genre: Genre, session: Session):
    genre.name = updated_genre.name
    genre.description = updated_genre.description
    session.add(genre)
    session.commit()
    session.refresh(genre)
    return genre