import sys

class PPlayingGame:

    def __init__(self, user):
        self._user = user
        self._objects = {}
        print('Created PlayingGame')


    def __len__(self):
        return len(self._objects)
    
    def __setitem__(self, key, value):
        self._objects[key] = value

    def __getitem__(self, key):
        return self._objects[key]  
		
    def send(self, message):
        user.send(message)
