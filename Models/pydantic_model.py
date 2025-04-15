from typing import List
from pydantic import BaseModel

class UserModel(BaseModel):
    Id: int
    discordId: int
    movieList: List[MovieModel]
    canDelete: bool
    
    

class MovieModel(BaseModel):
    Id: int