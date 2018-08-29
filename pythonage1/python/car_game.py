from pythonage.game import PGame
from car_playinggame import Car_PlayingGame

class Car_Game(PGame):

    def __init__(self):
        super().__init__() # First thing must be initialise our super class

    @property
    def gamename(self):
        return 'cargame'
    
    def get_playinggame(self, user, launch_info=None):
        return Car_PlayingGame(user, self, launch_info)


        
    
