import asyncio
import websockets

async def send_message():
    async with websockets.connect("ws://localhost:1500") as websocket:
        message = "Hi, Im C Kishan Koushik"
        await websocket.send(message)
        print("Message sent to server")

asyncio.get_event_loop().run_until_complete(send_message())