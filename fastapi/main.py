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
    # loft: Optional[str] = None
    # shaft_material: Optional[str] = None
    # shaft_flex: Optional[str] = None
    # length_inches: Optional[int] = None
    # grip_type: Optional[str] = None
    
class ShotsBase(BaseModel):
    club_id: int
    timestamp: datetime
    distance: int
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/clubs/", response_model=List[ClubsBase])
async def get_clubs(db: db_dependency, skip: int=0, limit: int=100):
    clubs=db.query(models.Clubs).offset(skip).limit(limit).all()
    return clubs

@app.get("/clubs/{club_id}")
async def get_question(club_id: int, db: db_dependency):
    result = db.query(models.Clubs).filter(models.Clubs.id == club_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Question not found")
    return result


@app.get("/shots/")
async def get_shots(db: db_dependency, skip: int=0, limit: int=100):
    shots=db.query(models.Shots).offset(skip).limit(limit).all()
    return shots

@app.post("/add/club/")
async def add_club(club: ClubsBase, db: db_dependency):
    db_club = models.Clubs(
        brand = club.brand,
        model = club.model,
        club_type = club.club_type
        # loft = club.loft,
        # shaft_material = club.shaft_material,
        # shaft_flex = club.shaft_flex,
        # length_inches = club.length_inches,
        # grip_type = club.grip_type
    )
    db.add(db_club)
    db.commit()
    db.refresh(db_club)

@app.post("/add/shot/")
async def add_shot(shot: ShotsBase, db: db_dependency):
    db_shots = models.Clubs(
        club_id = shot.club_id,
        timestamp = shot.timestamp,
        distance = shot.distance
    )
    db.add(db_shots)
    db.commit()
    db.refresh(db_shots)