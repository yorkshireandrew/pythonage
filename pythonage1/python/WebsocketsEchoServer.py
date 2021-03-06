#!/usr/bin/env python

import asyncio
import websockets

async def echo(websocket, path):
    count = 0
    async for message in websocket:
        print(message)
        count += 1
        print(str(count))
        #await websocket.send(message)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()
