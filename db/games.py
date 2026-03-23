from datetime import date, time
from typing import Optional, Union

from sqlalchemy import Column, String, Date, Time, Integer, Float

from db.base import Base

class Game (Base):
    __tablename__ = "game"

    id = Column("pk_id", Integer, primary_key=True)
    imageUrl = Column("image_url", String(2083))
    gameTitle = Column("game_title", String(50), nullable=False)
    developer = Column(String(50), nullable=False)
    platform = Column(String(30), nullable=False)
    gameUrl = Column("game_url", String(2083))
    startDate = Column("start_date", Date)
    startTime = Column("start_time", Time)
    finishDate = Column("finish_date", Date)
    finishTime = Column("finish_time", Time)
    score = Column(Float)

    # LEMBRETE: REVISAR TIPOS 

    def __init__(self, 
                 imageUrl:Union[str, None], 
                 gameTitle:str, 
                 developer:str,
                 platform:str,
                 gameUrl:Union[str, None],  
                 startDate:Union[Date, None]=None,
                 startTime:Union[Time, None]=None,
                 finishDate:Union[date, None]=None, 
                 finishTime:Union[Time, None]=None,
                 score:float=None):
        
        """Adds a new game to the register.

        Args:
            imageUrl (Optional[str]): Game image Url.
            gameTitle (str): Game's title.
            developer (str): Game's developer.
            platform (String): Game's platform (e.g. Nintendo 64).
            gameUrl (Optional[str]): Game Url.
            startDate (Optional[date]): Date the user started the game.
            startTime (Optional[time]): Time the user started the game.
            finishDate (Optional[date]): Date the user finished the game.
            finishTime (Optional[time]): Time the user finished the game.
            score (Optional[float]): Score given by the user (0-5).
        """
        self.imageUrl =  imageUrl or None
        self.gameTitle = gameTitle
        self.developer = developer 
        self.platform = platform
        self.gameUrl = gameUrl or None
        self.startDate = startDate 
        self.startTime = startTime 
        self.finishDate = finishDate 
        self.finishTime = finishTime
        self.score = score 
