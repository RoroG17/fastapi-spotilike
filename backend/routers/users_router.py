from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from db.db import get_session

from models.user_model import User
from models.auth_model import Token

from repository.users_repository import *

from fastapi.security import OAuth2PasswordRequestForm
from auth import create_access_token, get_current_user

router = APIRouter()

@router.post("/api/users/signup")
def signup_user(user: User, session: Session = Depends(get_session)):
    user = post_user(session, user)
    return {"message": "User created successfully"}

@router.post("/api/users/login", response_model=Token)
def login_user(user_credentials : OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user = verify_user_credentials(session, user_credentials.username, user_credentials.password)
    if user :
        token = create_access_token(data={"user_id": user.id})
        return {"message": "Login successful", "access_token": token, "token_type": "bearer"}
    return {"error": "Invalid credentials"}

@router.delete("/api/users/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_session), current_user: int =Depends(get_current_user)):
    user = get_user_by_id(session, user_id)
    if user:
        del_user(session, user)
        return {"message": "User deleted successfully", "code": 200}
    return {"error": "User not found", "code": 404}