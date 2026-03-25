from datetime import date, time
from typing import Optional, Union

from sqlalchemy import Column, String, Date, Time, Integer, Float

from db.base import Base

class Game (Base):
    __tablename__ = "game"

    id = Column("pk_id", Integer, primary_key=True)
    imageUrl = Column("image_url", String(2083), nullable=True)
    gameTitle = Column("game_title", String(50), nullable=False)
    developer = Column(String(50), nullable=False)
    platform = Column(String(30), nullable=False)
    gameUrl = Column("game_url", String(2083), nullable=True)
    startDate = Column("start_date", Date, nullable=True)
    startTime = Column("start_time", Time, nullable=True)
    finishDate = Column("finish_date", Date, nullable=True)
    finishTime = Column("finish_time", Time, nullable=True)
    score = Column(Float, nullable=True)

    # LEMBRETE: REVISAR TIPOS 

    def __init__(self, 
                 imageUrl:Optional[String], 
                 gameTitle:String, 
                 developer:String,
                 platform:String,
                 gameUrl:Optional[String],  
                 startDate:Optional[Date],
                 startTime:Optional[Time],
                 finishDate:Optional[Date], 
                 finishTime:Optional[Time],
                 score:Optional[Float]):
        """Adds a new game to the register.

        Args:
            imageUrl (Optional[String]): Game image Url.
            gameTitle (String): Game's title.
            developer (String): Game's developer.
            platform (String): Where the game has been played.
            gameUrl (Optional[String]): Game URL.
            startDate (Optional[Date]): Date the user started the game.
            startTime (Optional[Time]): ime the user started the game.
            finishDate (Optional[Date]):  Date the user finished the game.
            finishTime (Optional[Time]): Time the user finished the game.
            score (Optional[Float]): Score given by the user (0-5).
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
