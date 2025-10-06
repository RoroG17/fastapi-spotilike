from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./spotilike.db"
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

        
if __name__ == "__main__":
    init_db()
    print("✅ Base de données initialisée !")