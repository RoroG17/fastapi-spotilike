# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.artistes_router import router as artistes_router
from routers.albums_router import router as albums_router
from routers.genres_router import router as genres_router
from routers.users_router import router as users_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["http://localhost:9000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(artistes_router)
app.include_router(albums_router)
app.include_router(genres_router)
app.include_router(users_router)



