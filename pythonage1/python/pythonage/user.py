import sys

class PUser:

    def __init__(self, name, websocket, polling_scheduler):
        self.name = name
        self._websocket = websocket
        self._polling_scheduler = polling_scheduler   
        print('Created User ' + name)
		
    def send(self, message):
        if self.websocket:
            self.websocket.send(message)
        else:
            print('User ' + self.name + ' fake message send: ' + message) 

