import sys

class PUser:

    def __init__(self, user_id, websocket, polling_scheduler):
        self.user_id = user_id
        self._websocket = websocket
        self._polling_scheduler = polling_scheduler
        self.pending_messages = [];
        self.render_based_flushing = False;
        print('Created User ' + name)
		
    def send(self, message):
        if self.render_based_flushing:
            websocket.send(message)
        else:
            self.pending_messages.append(message)
            print('User {0} queued message: {1}'.format(self.user_id, message))        
        
        if self.websocket:
            self.websocket.send(message)
        else:
            print('User {0} faked message send: {1}'.format(self.user_id, message))

