import asyncio
import websockets

async def send_message(websocket, path):
    message = "Im a going to graduate in June 2024 from Mahindra University"
    await websocket.send(message)
    print("Message sent to client")

start_server = websockets.serve(send_message, "localhost", 3000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()