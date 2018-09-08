#!/usr/bin/env python3

import asyncio
import websockets

# Websocket server used during early testing to see what we got sent
async def handle_connect(websocket, path):
    
    count = 0
    async for message in websocket:
        print(message)
        count += 1
        print(str(count))
        #await websocket.send(message)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(handle_connect, 'localhost', 8765))
asyncio.get_event_loop().run_forever()
