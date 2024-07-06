from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, DateTime, Null
    
class Clubs(Base):
    __tablename__ = 'clubs'
    
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String)
    model = Column(String)
    club_type = Column(String)