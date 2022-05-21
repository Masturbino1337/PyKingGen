import asyncio
from pykinggen import Client

client = Client("api-key")

async def main():
    return print(await client.alt())

asyncio.run(main())
