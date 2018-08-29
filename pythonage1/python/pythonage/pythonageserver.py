#!/usr/bin/env python3

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed
from .user import PUser

class PythonageServer:

    def __init__(self, game_factory):
        
        self._game_factory = game_factory
        self._user_id = 0
        self._users = {}
        self._send_messages_task = asyncio.ensure_future(self._send_all_user_messages())
        self._ticking_timers_task = asyncio.ensure_future(self.ticking_task_async())

    async def handle_connect(self, websocket, path):
        
        user = PUser(self._user_id, websocket, self._game_factory)
        self._user_id += 1
        try:
            message = await websocket.recv() # First message should tell us what game the client wants
            print('PythonageServer got message: {0}'.format(message))

            # Use our game factory to create a playing game for us
            frags = message.split(',')
            game_name = frags[1]

            user.launch_playinggame_from_gamefactory(game_name, launch_info=None)

            self._users[user.user_id] = user # Add ourselves to the dictionary of users so users can send messages
            await user.listen_to_websocket_async()
        except websockets.exceptions.ConnectionClosed:
            del self._users[user.user_id]
       

    async def _send_all_user_messages(self):
        
        while True:
            while self._users.items():
                for key, user in self._users.items():
                    await user.send_async()
                await asyncio.sleep(0.01) # 10ms
            await asyncio.sleep(0.5) # Relax we have no users

    def _tick(self): # Periodically called by ticking_task_async
        
        for key, user in self._users.items():
            user.tick()

    async def ticking_task_async(self):
        
        try:
            while True:
                while self._users.items():
                    self._tick()
                    await asyncio.sleep(0.01) # 10ms tick
                await asyncio.sleep(0.5) # Relax we have no users
        except Exception as e:
            tb = traceback.format_exc()
            print('===== TICKING TASK SWALLOWED EXCEPTION ===')
            print(tb)
            print('===================================')
        print('ticking_task_async completed!') # Should never happen
            
