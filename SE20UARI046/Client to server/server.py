import asyncio
import websockets

async def receive_message(websocket, path):
    message = await websocket.recv()
    print(f"Message received from client: {message}")

start_server = websockets.serve(receive_message, "localhost", 1500)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()