import sys

# Encapsulates communication with a user via a websocket connection
# and provides a way for a playing game to hook into the servers services.
class PUser:

    def __init__(self, user_id, websocket):
        self.user_id = user_id
        self._websocket = websocket
        self.pending_messages = []
        self.flush_on_render = False
        self._playing_game = None
        self._keys = {}
        print('Created User ' + name)

    def set_playing_game(self, playing_game):
        self._playing_game = playing_game
        
    # Send a message to the user, buffering them if flush_on_render is enabled
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
            print('User {0} sending message: {1}'.format(self.user_id, message))
            websocket.send(message)


    # Coroutine that continually listens to websocket, exiting only when the client says byebye
    async def listen_to_websocket_async(self):
        message = await self._websocket.recv()
        while not message == 'byebye':
            fragments = message.split(',')
            command = fragments[0]

            # Response to a key query
            if command == 'qk':
                fragment_iterator = iter(fragments)
                fragment_iterator.next() # Skip over the command
                try:
                    key = fragment_iterator.next()
                    pressed_string = fragment_iterator.next()
                    self._keys[key] = pressed_string == 't'
                except StopIteration:
                    pass

            elif command == 'il':
                object_id = fragments[1]
                self._playing_game.handle_imagedata_loaded(object_id)

            message = await self._websocket.recv()
