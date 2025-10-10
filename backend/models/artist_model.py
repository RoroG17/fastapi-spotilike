from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class Artist(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    avatar: str
    bio: str

    musics: List["Music"] = Relationship(back_populates="artist")
    albums: List["Album"] = Relationship(back_populates="artist")
