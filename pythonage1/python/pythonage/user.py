import sys
from collections import deque

# Encapsulates communication with a user via a websocket connection
# and provides a way for a playing game to hook into the servers services.
class PUser:

    def __init__(self, user_id, websocket):
        self.user_id = user_id
        self._websocket = websocket

        # Additional construction
        self._stored_messages = deque()
        self._send_immediately_messages = deque()
        self.store_messages = False
        self._playing_game = None
        self._keys = {}
        print('Created User {0}'.format(user_id))

    def set_playing_game(self, playing_game):
        self._playing_game = playing_game
        
    # Send a message to the users browser, buffering them if store_messages is true. Allows double buffering.
    def send(self, message):
        
        if not self._websocket:
            print('User {0} faked message send: {1}'.format(self.user_id, message))
            return
        
        if self.store_messages:
            self._stored_messages.append(message)
        else:
            self._send_immediately_messages.append(message)

    # Send a message to the users browser immediately ignoring the store_messages field
    def send_immediately(self, message):
        
        self._send_immediately_messages.append(message)

    # Async call that the server uses to send all the queued messages
    async def send_async(self):
        websocket = self._websocket
        
        if not self.store_messages:
            while self._stored_messages:
                message = self._stored_messages.pop()
                async websocket.send(message)

        while self._send_immediately_messages:
            message = _send_immediately_messages.pop()
            async websocket.send(message)


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
