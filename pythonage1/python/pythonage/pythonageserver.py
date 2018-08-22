#!/usr/bin/env python3

import asyncio
import websockets
from gamefactory import *
from serverservices import *
from user import *

class PythonageServer:

    def __init__(self, game_factory):
        self._game_factory = game_factory
        self._server_services = PServerServices()
        self._user_id = 0


    async def handle_connect(self, websocket, path):
        user = PUser(self._user_id, websocket)
        self._user_id += 1
        message = await websocket.recv() # First message should tell us what game the client wants
        print('PythonageServer got message: {0}'.format(message))

        # Use our game factory to create a playing game for us
        frags = message.split(',')
        game_name = frags[1]
        playing_game = self._game_factory.get_playinggame(game_name, user, self._server_services)

        await user.listen_to_websocket_async()     

game_factory = PGameFactory()
pythonage_server = PythonageServer(game_factory)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(pythonage_server.handle_connect, 'localhost', 8765))
asyncio.get_event_loop().run_forever()
