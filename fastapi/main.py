from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated, Optional, Dict, Any
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ClubsBase(BaseModel):
    brand: str
    model: str
    club_type: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/clubs/", response_model=List[ClubsBase])
async def get_clubs(db: db_dependency, skip: int = 0, limit: int = 100):
    clubs = db.query(models.Clubs).offset(skip).limit(limit).all()
    return clubs


@app.post("/add/club/")
async def add_club(club: ClubsBase, db: db_dependency):
    db_club = models.Clubs(brand=club.brand, model=club.model, club_type=club.club_type)
    db.add(db_club)
    db.commit()
    db.refresh(db_club)
    return {"message": "Club added successfully"}


@app.delete("/delete/club/")
async def delete_club(club_id: int, db: db_dependency):
    db_club = db.query(models.Clubs).filter(models.Clubs.id == club_id).first()
    db.delete(db_club)
    db.commit()
    return {"message": "Club deleted successfully"}
