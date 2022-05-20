import asyncio
from pyking import Client

client = Client("api-key")

async def main():
    return print(await client.profile())

asyncio.run(main())
