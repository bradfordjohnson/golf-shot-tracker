from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, DateTime, Null

# class Users(Base):
#     __tablename__ = 'users'
    
#     id = Column(Integer, primary_key=True, index=True)
#     first_name = Column(String)
#     last_name = Column(String)
    
class Clubs(Base):
    __tablename__ = 'clubs'
    
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String)
    model = Column(String)
    club_type = Column(String)
    # loft = Column(String)
    # shaft_material = Column(String)
    # shaft_flex = Column(String)
    # length_inches = Column(Integer)
    # grip_type = Column(String)
    
class Shots(Base):
    __tablename__ = 'shots'
    
    id = Column(Integer, primary_key=True, index=True)
    club_id =  Column(Integer, ForeignKey("clubs.id"))
    timestamp = Column(DateTime)
    # location
    # measurement_method
    # unit
    distance = Column(Integer)
    # shot_type = Column(String)
    # notes = Column(String)