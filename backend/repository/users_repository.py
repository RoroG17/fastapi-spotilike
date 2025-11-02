from sqlalchemy.orm import Session
from models.user_model import User

def get_user_by_id(session: Session, user_id: int):
    return session.get(User, user_id)

def get_user_by_username(session: Session, username: str):
    return session.query(User).filter(User.username == username).first()

def verify_user_credentials(session: Session, username: str, password: str):
    user = get_user_by_username(session, username)
    if user and user.hashed_password == password:
        return user
    return None

def post_user(session: Session, user: User):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def del_user(session: Session, user: User):
    if user:
        session.delete(user)
        session.commit()
        return True
    return False

