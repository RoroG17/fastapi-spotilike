from datetime import date, time
from sqlmodel import Session
from db.db import engine, init_db
from models.artist_model import Artist
from models.music_model import Music
from models.album_model import Album
from models.genre_model import Genre
from models.user_model import User

# 1️⃣ Crée les tables si nécessaire
init_db()

with Session(engine) as session:

    # -------------------
    # GENRES
    # -------------------
    genre1 = Genre(name="Pop", description="Musique populaire")
    genre2 = Genre(name="Rock", description="Musique rock")
    genre3 = Genre(name="Jazz", description="Musique jazz")
    genre4 = Genre(name="Rap", description="Musique rap")
    genre5 = Genre(name="Classique", description="Musique classique")
    session.add_all([genre1, genre2, genre3, genre4, genre5])
    session.commit()
    session.refresh(genre1)
    session.refresh(genre2)
    session.refresh(genre3)
    session.refresh(genre4)
    session.refresh(genre5)

    # -------------------
    # ARTISTES
    # -------------------
    artist1 = Artist(name="Taylor Swift", avatar="taylor.png", bio="Pop singer")
    artist2 = Artist(name="Ed Sheeran", avatar="ed.png", bio="Singer-songwriter")
    artist3 = Artist(name="Miles Davis", avatar="miles.png", bio="Jazz trumpeter")
    artist4 = Artist(name="Eminem", avatar="eminem.png", bio="Rap artist")
    artist5 = Artist(name="Ludovico Einaudi", avatar="ludovico.png", bio="Pianist")
    session.add_all([artist1, artist2, artist3, artist4, artist5])
    session.commit()
    session.refresh(artist1)
    session.refresh(artist2)
    session.refresh(artist3)
    session.refresh(artist4)
    session.refresh(artist5)

    # -------------------
    # ALBUMS
    # -------------------
    album1 = Album(title="Fearless", cover="fearless.png", release_year=date(2008, 11, 11), artist_id=artist1.id)
    album2 = Album(title="Divide", cover="divide.png", release_year=date(2017, 3, 3), artist_id=artist2.id)
    album3 = Album(title="Kind of Blue", cover="kindofblue.png", release_year=date(1959, 8, 17), artist_id=artist3.id)
    album4 = Album(title="The Marshall Mathers LP", cover="mmlp.png", release_year=date(2000, 5, 23), artist_id=artist4.id)
    album5 = Album(title="Divenire", cover="divenire.png", release_year=date(2006, 1, 1), artist_id=artist5.id)
    session.add_all([album1, album2, album3, album4, album5])
    session.commit()
    session.refresh(album1)
    session.refresh(album2)
    session.refresh(album3)
    session.refresh(album4)
    session.refresh(album5)

    # -------------------
    # MORCEAUX
    # -------------------
    morceau1 = Music(title="Love Story", duration=time(0,3,55), genre_id=genre1.id, album_id=album1.id, artist_id=artist1.id)
    morceau2 = Music(title="Shape of You", duration=time(0,4,24), genre_id=genre1.id, album_id=album2.id, artist_id=artist2.id)
    morceau3 = Music(title="So What", duration=time(0,9,22), genre_id=genre3.id, album_id=album3.id, artist_id=artist3.id)
    morceau4 = Music(title="Stan", duration=time(0,6,44), genre_id=genre4.id, album_id=album4.id, artist_id=artist4.id)
    morceau5 = Music(title="Nuvole Bianche", duration=time(0,6,0), genre_id=genre5.id, album_id=album5.id, artist_id=artist5.id)
    session.add_all([morceau1, morceau2, morceau3, morceau4, morceau5])
    session.commit()

    print("✅ Jeu de test inséré avec succès !")

    # -------------------
    # UTILISATEURS
    # -------------------

    user1 = User(username="admin", email="admin@admin", hashed_password="1234")
    session.add(user1)
    session.commit()
