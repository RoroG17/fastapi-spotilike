from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date

class Album(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    cover: str
    release_year: date
    artist_id: Optional[int] = Field(default=None, foreign_key="artist.id")

    artist: Optional["Artist"] = Relationship(back_populates="albums")
    musics: List["Music"] = Relationship(back_populates="album")
