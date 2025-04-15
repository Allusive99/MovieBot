from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
class User(Base):
    __tablename__ = "Users"
    DiscordId = Column(Integer, primary_key=True)
    CanAdd = Column(Boolean)
    CanDelete = Column(Boolean)

class Movie(Base):
    __tablename__ = "Movies"
    MovieId = Column(Integer, primary_key=True)
    Name = Column(String)
    Genre = Column(String)
    Director = Column(String)
    
class WatchList(Base):
    __tablename__ = "WatchList"
    ListId = Column(Integer, primary_key=True)
    UserId = Column(Integer, ForeignKey("Users.DiscordId"))
    Name = Column(String)
    Genre = Column(String)
    Director = Column(String)
    
    user = relationship("User", backref="watchlists")