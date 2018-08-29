from pythonage.game import PGame
from carlobby_playinggame import CarLobby_PlayingGame

class CarLobby_Game(PGame):

    def __init__(self):
        super().__init__() # First thing must be initialise our super class

    @property
    def gamename(self):
        return 'carlobbygame'
    
    def get_playinggame(self, user, launch_info):
        return CarLobby_PlayingGame(user, self)


        
    
