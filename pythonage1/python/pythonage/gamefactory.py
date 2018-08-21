from cargame import *

class PGameFactory:

    def __init__(self):
        self._games = {}

        self._games['cargame'] = new CarGame()

    def get_usergame(self, gamename, websocket):
        try:
            game = self._games[gamename]
            return game.get_usergame(websocket)
        except KeyError:
            return None
