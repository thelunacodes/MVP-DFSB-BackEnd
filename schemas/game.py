from datetime import date, time

from pydantic import BaseModel
from typing import Optional, List

from db.games import Game

class GameSchema(BaseModel):
    """ Defines how the registered game should be represented.
    """

    imageUrl:Optional[str] = None
    gameTitle:str 
    developer:str 
    platform:str 
    gameUrl:Optional[str] = None
    startDate:Optional[date] = None 
    startTime:Optional[time] = None 
    finishDate:Optional[date] = None 
    finishTime:Optional[time] = None 
    score: Optional[float] = None

class UpdateSchema(BaseModel):
    """ Defines how the updated game should be represented.
    """

    id:int 
    imageUrl:Optional[str] = None
    gameTitle:str 
    developer:str 
    platform:str 
    gameUrl:Optional[str] = None
    startDate:Optional[date] = None 
    startTime:Optional[time] = None 
    finishDate:Optional[date] = None 
    finishTime:Optional[time] = None 
    score: Optional[float] = None

class GameDeletionSchema(BaseModel):
    """ Defines how the game deletion should be structured."""

    id:int = 1

class GameIdSearch(BaseModel):
    """ Defines how the game id search should be structured.
    """

    id:int = 1

class GameListingSchema(BaseModel):
    """ Defines how the game search result should be structured.
    """
    
    games:List[GameSchema]

def show_games(games: List[Game]):
    """ Returns:
        dict: The representation of a game, following
            the structure defined in GameViewSchema.
    """

    result = []
    for game in games:
        result.append({
            "id": game.id,
            "imageUrl":game.imageUrl,
            "gameTitle":game.gameTitle,
            "developer":game.developer,
            "platform":game.platform,
            "gameUrl":game.gameUrl,
            "gameUrl": game.gameUrl,
        "startDate": game.startDate.isoformat() if game.startDate else None,
        "startTime": game.startTime.strftime("%H:%M") if game.startTime else None,
        "finishDate": game.finishDate.isoformat() if game.finishDate else None,
        "finishTime": game.finishTime.strftime("%H:%M") if game.finishTime else None,
            "score":game.score,
        })
        
    return {"games": result}
    
class GameViewSchema(BaseModel):
    """ Defines how the game data should be returned.
    """

    id:int 
    imageUrl:Optional[str] 
    gameTitle:str 
    developer:str
    platform:str 
    gameUrl:Optional[str] 
    startDate:Optional[date] 
    startTime:Optional[time] 
    finishDate:Optional[date] 
    finishTime:Optional[time] 
    score: Optional[float] 

class GameDelSchema(BaseModel):
    """ Defines the structure of the data returned 
        after a deletion request.
    """

    message:str
    gameTitle:str

def show_game(game:Game):
    """ Returns :
            dict: a representation of a game, following the 
                  structure defined in GameViewSchema.
    """

    return {
        "id": game.id,
        "imageUrl":game.imageUrl,
        "gameTitle":game.gameTitle,
        "developer":game.developer,
        "platform":game.platform,
        "gameUrl":game.gameUrl,
        "gameUrl": game.gameUrl,
        "startDate": game.startDate.isoformat() if game.startDate else None,
        "startTime": game.startTime.strftime("%H:%M") if game.startTime else None,
        "finishDate": game.finishDate.isoformat() if game.finishDate else None,
        "finishTime": game.finishTime.strftime("%H:%M") if game.finishTime else None,
        "score":game.score,
    }
