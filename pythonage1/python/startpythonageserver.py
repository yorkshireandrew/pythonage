#!/usr/bin/env python3
import asyncio
import websockets

from pythonage.pythonageserver import PythonageServer
from pythonage.gamefactory import PGameFactory
from car_game import Car_Game
from carlobby_game import CarLobby_Game

if __name__ == '__main__':
    
    game_factory = PGameFactory()
    game_factory.register_game(Car_Game())
    game_factory.register_game(CarLobby_Game())

    pythonage_server = PythonageServer(game_factory)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(websockets.serve(pythonage_server.handle_connect, 'localhost', 8765))
    loop.run_forever()
