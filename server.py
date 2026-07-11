import asyncio
import json
import websockets

clients = set()

async def handler(ws):
    clients.add(ws)

    try:
        async for message in ws:
            data = json.loads(message)

            # 全員に送信
            for client in clients:
                await ws.send(data)

    finally:
        clients.remove(ws)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 1229):
        await asyncio.Future()

asyncio.run(main())
