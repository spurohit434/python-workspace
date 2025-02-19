import aiohttp
import asyncio

async def fetch_page(url):
    async with aiohttp.ClientSession() as session:   #this will create an session
        async with session.get(url) as response:
            print(response)


loop = asyncio.get_event_loop()
loop.run_until_complete(fetch_page('https://www.geeksforgeeks.org/python-programming-language/'))