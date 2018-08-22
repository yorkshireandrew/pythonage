from car_game import *

class PGameFactory:

    def __init__(self):
        self._games = {}
        self.register_game('cargame', Car_Game())
        

    def register_game(self, game_name, game):
        print('Registered game ' + game_name)
        self._games[game_name] = game  

    def get_playinggame(self, gamename, user, server_services):
        print('get playinggame called')
        try:
            game = self._games[gamename.strip()]
        except KeyError:
            print('User asked for game {0} but it was not registered in PGameFactory'.format(gamename))
            return None
        
        return game.get_playinggame(user, server_services)

