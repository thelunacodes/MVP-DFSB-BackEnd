from datetime import datetime

from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from db import Session, Game
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Game Backlog API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentation",
               description="Select type of documentation (Swagger, Redoc or Rapidoc)")
game_tag = Tag(name="Game", 
               description="Manage games registered to the database")


@app.get('/', tags=[home_tag])
def home():
    """ Redirect user to '/openapi', where the documentation style is chosen.
    """

    return redirect('/openapi')

@app.post('/game', tags=[game_tag])
def add_game(form:GameSchema):
    """ Adds a new game to the database.
        
        Returns:
            dict: A representation of the newly added game.
    """
    
    game = Game(
        imageUrl=form.imageUrl,
        gameTitle=form.gameTitle,
        developer=form.developer,
        platform=form.platform,
        gameUrl=form.gameUrl,
        startDate=form.startDate,
        startTime=form.startTime,
        finishDate=form.finishDate,
        finishTime=form.finishTime,
        score=form.score
    )

    logger.debug(f"Adding a new game: '{game.gameTitle}'")

    try:
        session = Session()
        session.add(game)
        session.commit()

        logger.debug(f"Added game: '{game.gameTitle}") 
        return show_game(game), 200
    except IntegrityError as err:
        logger.warning(f"IntegrityError at 'add_game': {err}")
        return {"message": str(err)}, 409
    except Exception as ex:
        logger.warning(f"Unable to save new game: {ex}")
        return {"message": str(ex)}, 400
    
@app.get('/games', tags=[game_tag],
         responses={"200": GameListingSchema, "404": ErrorSchema })
def get_games():
    """  Retrieves all registered games. 

    Returns:
        dict: Dictionary with all the registered games.
    """

    logger.debug("Searching games...")

    session = Session()

    games = session.query(Game).all()

    if not games:
        return { "games": []}, 404
    else:
        logger.debug(f"{len(games)} games found!")
        # print(games)
        return show_games(games), 200
    
@app.get('/game', tags=[game_tag],
            responses={"200": GameViewSchema, "404": ErrorSchema})
def get_game(query: GameIdSearch):
    """ Retrieves a game by its id. 

        Returns: 
            dict: The game representation, if found.

    """
    gameId = query.id
    logger.debug(f"Searching for '{gameId}'...")

    session = Session()
    
    game = session.query(Game).filter(Game.id == gameId).first()

    if not game:
        logger.warning(f"Game with ID {gameId} was not found.")
        return {"message": "Couldn't fetch the game by its ID."}, 404
    else:
        logger.debug(f"Game found: '{game.gameTitle}'")
        return show_game(game), 200

@app.put('/game', tags=[game_tag],
         responses={"200": GameViewSchema, "404": ErrorSchema})
def update_game(form: UpdateSchema):
    """Updates a game by its ID.
    """

    gameId = form.id
    logger.debug(f"Updating game with ID: {gameId}")

    session = Session()
    game = session.query(Game).filter(Game.id == gameId).first()

    if not game:
        return {"message": "Game not found"}, 404

    try:
        game.imageUrl = form.imageUrl
        game.gameTitle = form.gameTitle
        game.developer = form.developer
        game.platform = form.platform
        game.gameUrl = form.gameUrl
        game.startDate = form.startDate
        game.startTime = form.startTime
        game.finishDate = form.finishDate
        game.finishTime = form.finishTime
        game.score = form.score

        session.commit()
        return show_game(game), 200
    except Exception as ex:
        logger.warning(f"Unable to update game: {ex}")
        return {"message": str(ex)}, 400


@app.delete('/game', tags=[game_tag],
            responses={"200": GameDelSchema, "404":ErrorSchema})
def delete_game(query: GameDeletionSchema):
    """
        Returns:
            dict: Dictionary with the result of the 
                  deletion request, or an error message.
    """

    gameId = query.id
    logger.debug(f"Deleting game: '{query.gameTitle}'")

    session = Session()
    delGame = session.query(Game).filter(Game.id == gameId).delete()
    session.commit()

    if delGame:
        logger.debug(f"Game deleted successfuly: '{query.gameTitle}'")
        return {"message": "Game deleted.", "gameTitle": query.gameTitle}, 200
    else:
        logger.warning(f"There's no game with id {query.id}")
        return {"message": f"There's no game with id {query.id}"}, 404