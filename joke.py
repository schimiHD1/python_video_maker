from jokeapi import Jokes
import asyncio

def run():
    jokes = asyncio.run(get_jokes())
    return(jokes)

async def get_jokes():
    j = await Jokes()
    raw = await j.get_joke()
    if raw["type"] == "twopart":
        return(raw["setup"],raw["delivery"])
        

if __name__ == "__main__":
    print(run())