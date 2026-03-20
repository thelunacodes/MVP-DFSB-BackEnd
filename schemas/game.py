from datetime import date, time

from pydantic import BaseModel
from typing import Optional, List

from db.games import Game

class GameSchema(BaseModel):
    """ Defines how the registered game should be represented.
    """

    imageUrl:Optional[str] = "https://www.connetweb.com/wp-content/uploads/2021/06/canstockphoto22402523-arcos-creator.com_-1024x1024-1-600x600.jpg"
    gameTitle:str = "Game Name"
    developer:str = "Developer"
    publisher:Optional[str] = "Publisher"
    platform:str = "Nintendo DS"
    gameUrl:Optional[str] = "https://www.google.com"
    startDate:Optional[date] = None
    startTime:Optional[time] = None
    finishDate:Optional[date] = None
    finishTime:Optional[time] = None
    score: Optional[float] = 5.0

class GameDeletionSchema(BaseModel):
    """ Defines how the game deletion should be structured."""

    id:int = 1
    gameTitle:str = "Game Name"

class GameSearchSchema(BaseModel):
    """ Defines how the game search should be structured.
    """

    gameTitle:str = "Game Name"

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
            "imageUrl":game.imageUrl,
            "gameTitle":game.gameTitle,
            "developer":game.developer,
            "publisher":game.publisher,
            "platform":game.platform,
            "gameUrl":game.gameUrl,
            "startDate":game.startDate,
            "startTime":game.startTime,
            "finishDate":game.finishDate,
            "finishTime":game.finishTime,
            "score":game.score,
        })
        
    return {"games": result}
    
class GameViewSchema(BaseModel):
    """ Defines how the game data should be returned.
    """

    id:int = 1
    imageUrl:Optional[str] = "https://www.connetweb.com/wp-content/uploads/2021/06/canstockphoto22402523-arcos-creator.com_-1024x1024-1-600x600.jpg"
    gameTitle:str = "Game Name"
    developer:str = "Developer"
    publisher:Optional[str] = "Publisher"
    platform:str = "Nintendo DS"
    gameUrl:Optional[str] = "https://www.google.com"
    startDate:Optional[date] = None
    startTime:Optional[time] = None
    finishDate:Optional[date] = None
    finishTime:Optional[time] = None
    score: Optional[float] = 5.0

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
        "publisher":game.publisher,
        "platform":game.platform,
        "gameUrl":game.gameUrl,
        "startDate":game.startDate,
        "startTime":game.startTime,
        "finishDate":game.finishDate,
        "finishTime":game.finishTime,
        "score":game.score,
    }
