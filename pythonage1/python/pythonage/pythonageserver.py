#!/usr/bin/env python3

import asyncio
import websockets
from gamefactory import *
from user import *

class PythonageServer:

    def __init__(self, game_factory):
        self._game_factory = game_factory
        self._user_id = 0
        self._users = []
        self._send_messages_task = asyncio.ensure_future(self._send_all_user_messages())

    async def handle_connect(self, websocket, path):
        user = PUser(self._user_id, websocket)
        self._user_id += 1
        message = await websocket.recv() # First message should tell us what game the client wants
        print('PythonageServer got message: {0}'.format(message))

        # Use our game factory to create a playing game for us
        frags = message.split(',')
        game_name = frags[1]
        playing_game = self._game_factory.get_playinggame(game_name, user)

        # Route traffic from the user to the game
        user.set_playing_game(playing_game)

        self._users.append(user) # Add ourselves to the list of users so users can send messages
        await user.listen_to_websocket_async()

    async def _send_all_user_messages(self):
        while True:
            while self._users:
                for user in self._users:
                    await user.send_async()
                await asyncio.sleep(0.01) # 10ms

            #print('waiting for users')
            await asyncio.sleep(0.5) # Relax we have no users

    def _tick(self): # Periodically called by ticking_task_async
        for user in self._users:
            user.tick()

    async def ticking_task_async(self):
        while True:
            while self._users:
                self._tick()
                await asyncio.sleep(0.01) # 10ms tick

            await asyncio.sleep(0.5) # Relax we have no users

game_factory = PGameFactory()
pythonage_server = PythonageServer(game_factory)

loop = asyncio.get_event_loop()
loop.create_task(pythonage_server.ticking_task_async())
loop.run_until_complete(websockets.serve(pythonage_server.handle_connect, 'localhost', 8765))
loop.run_forever()
