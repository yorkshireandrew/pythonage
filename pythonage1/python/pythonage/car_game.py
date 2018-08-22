from game import *
from car_playinggame import *

class Car_Game(PGame):

    def __init__(self):
        super().__init__() # First thing must be initialise our super class
        
    def get_playinggame(self, user, server_services):
        return Car_PlayingGame(user, server_services)


        
    
