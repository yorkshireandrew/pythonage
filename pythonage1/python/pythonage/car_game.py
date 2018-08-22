from car_playinggame import *
import time

class Car_Game(PGame):

    def __init__(self, user):
        super(PGame, self).__init__(user) # First thing must be initialise our super class
        
    def get_playinggame(self, user, server_services):
        return Car_PlayingGame(user, server_services)


        
    
