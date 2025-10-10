from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Genre(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str

    musics: List["Music"] = Relationship(back_populates="genre")