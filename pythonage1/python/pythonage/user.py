import sys
from collections import deque
from .timercollection import PTimerCollection

# Encapsulates communication with a user via a websocket connection
# and provides a way for a playing game to hook into the servers services.
class PUser:

    def __init__(self, user_id, websocket, game_factory):
        
        self.user_id = user_id
        self._websocket = websocket
        self._game_factory = game_factory
        self._reset()
        
        # print('Created User {0}'.format(user_id))

    def _reset(self):
        
        # Construct or set state as though it were our first connection to the browser-playinggame
        self._timer_collection = PTimerCollection()
        self._stored_messages = deque()
        self._send_immediately_messages = deque()
        self.store_messages = False
        self._playing_game = None
        self._keypresses = {}
        self._new_click = False
        self._new_click_x = 0
        self._new_click_y = 0
        self._render_complete_notification = False
        self.rendering = False
        
    # Send a message to the users browser, buffering them if store_messages is true. Allows double buffering.
    def send(self, message):
        
        if not self._websocket:
            print('User {0} faked message send: {1}'.format(self.user_id, message))
            return
        
        if self.store_messages:
            # print('Adding to stored messages:' + message)
            self._stored_messages.append(message)
        else:
            # print('Adding to Immediate messages:' + message)
            self._send_immediately_messages.append(message)

    # Send a message to the users browser immediately ignoring the store_messages field
    def send_immediately(self, message):
        
        self._send_immediately_messages.append(message)

    # Async call that the server uses to send all the queued messages
    async def send_async(self):
        
        websocket = self._websocket       
        if not self.store_messages:
            while len(self._stored_messages):
                message = self._stored_messages.popleft()
                await websocket.send(message)
                
        while len(self._send_immediately_messages):
            message = self._send_immediately_messages.popleft()
            # print('sent: {0}'.format(message))
            await websocket.send(message)


    # Coroutine that continually listens to websocket, exiting only when the client says byebye
    async def listen_to_websocket_async(self):
        
        message = await self._websocket.recv()
        # print('User {0} recieved: {1}'.format(self.user_id, message))
        while not message == 'byebye':
            fragments = message.split(',')
            command = fragments[0]

            # Response to a key query
            if command == 'qk':
                fragment_iterator = iter(fragments)
                next(fragment_iterator) # Skip over the command
                try:
                    while True:
                        key = next(fragment_iterator)
                        pressed_string = next(fragment_iterator)
                        pressed = pressed_string == '1'
                        self._keypresses[key] = pressed
                        # print('{0}:{1}'.format(key,pressed))
                except StopIteration:
                    pass

            elif command == 'il':
                object_id = fragments[1]
                self._playing_game.handle_imagedata_loaded(int(object_id))

            elif command == 'cl':
                self._new_click = True
                self._new_click_x = int(fragments[1])
                self._new_click_y = int(fragments[2])

            elif command == 'rc':
                self.rendering = False

            message = await self._websocket.recv()
            # print('User {0} recieved: {1}'.format(self.user_id, message))

    def append_timer_to_server(self, timer):
        
        self._timer_collection.append(timer)

    def remove_timer_from_server(self, timer):
        
        self._timer_collection.remove(timer)

    def remove_all_timers_from_server(self):
        
        self._timer_collection.remove_all_timers()

    def tick(self):
        
        self._timer_collection.tick()

    def update_keys(self, key_list):
    
        if len(key_list):
            joined = ','.join(key_list)
            self.send_immediately('qk,{0}'.format(joined))

    def is_pressed(self, key):
        return self._keypresses.setdefault(key, False)

    @property
    def clicked(self):
        
        return self._new_click

    def reset_clicked(self):
        
        self._new_click = False 

    @property
    def click_x(self):
        
        return self._new_click_x

    @property
    def click_y(self):
        
        return self._new_click_y

    @property
    def render_complete_notification(self):
        
        return self._render_complete_notification

    @render_complete_notification.setter
    def render_complete_notification(self, new_value):
        
        if new_value:
            self._render_complete_notification = True
            self.send_immediately('srcn,t')
        else:
            self._render_complete_notification = False
            self.send_immediately('srcn,f')

    def log_on_client(self, message):
        
        to_send = message.replace(',','{{comma}}')
        to_send = to_send.replace('<','&lt;')
        to_send = to_send.replace('>','&gt;')
        self.send_immediately('log,{0}'.format(to_send))

    def remove_all_from_browser(self):
        
        self.send('ra')

    def launch_playinggame_from_gamefactory(self, game_name, launch_info):
        
        # Permits one game to act as a prequel or lobby for another
        self._reset()
        playing_game = self._game_factory.get_playinggame(game_name, self, launch_info=launch_info)
        self._playing_game = playing_game


    def connection_lost(self): # Called by the server when the connection drops
        
        self._playing_game.connection_lost()

        

        
