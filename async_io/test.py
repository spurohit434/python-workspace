import asyncio

async def fetch_data():
    await asyncio.sleep(2)
    print("Data received")

def print_val():
    print("flow reached")

asyncio.run(fetch_data())
print_val()
print("to the world")