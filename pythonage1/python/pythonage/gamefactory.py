# Class that the pythonage server queries for games when a user attaches

class PGameFactory:

    def __init__(self):
        
        self._games = {}
        
    def register_game(self, game):
        
        print('Registered game ' + game.gamename)
        self._games[game.gamename] = game  

    def get_playinggame(self, gamename, user, launch_info=None):
        
        try:
            game = self._games[gamename.strip()]
        except KeyError:
            print('User asked for game {0} but it was not registered in PGameFactory'.format(gamename))
            return None
        
        return game.get_playinggame(user, launch_info)

