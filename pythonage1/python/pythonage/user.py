import sys

# Encapsulates communication with a user via a websocket connection
# and provides a way for a playing game to hook into the servers services.
class PUser:

    def __init__(self, user_id, websocket, polling_scheduler):
        self.user_id = user_id
        self._websocket = websocket
        self._polling_scheduler = polling_scheduler
        self.pending_messages = []
        self.flush_on_render = False
        print('Created User ' + name)
		
    def send(self, message, is_rendering_message=False):
        if not self.websocket:
            print('User {0} faked message send: {1}'.format(self.user_id, message))
            return
        
        if self.flush_on_render:
            if is_rendering_message:
                for pending_message in self.pending_messages:
                    websocket.send(pending_message)
                websocket.send(message)
                self.pending_messages = []
            else:      
                self.pending_messages.append(message)
                print('User {0} queued message: {1}'.format(self.user_id, message))
        else:
            websocket.send(message)
