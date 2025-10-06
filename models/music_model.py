from typing import Optional
from datetime import time
from sqlmodel import SQLModel, Field, Relationship

class Music(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    duration: time
    artist_id: Optional[int] = Field(default=None, foreign_key="artist.id")
    genre_id: Optional[int] = Field(default=None, foreign_key="genre.id")
    album_id: Optional[int] = Field(default=None, foreign_key="album.id")

    artist: Optional["Artist"] = Relationship(back_populates="musics")
    genre: Optional["Genre"] = Relationship(back_populates="musics")
    album: Optional["Album"] = Relationship(back_populates="musics")
    
