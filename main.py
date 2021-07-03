import asyncio
from utils import setup

session, client = setup()


async def get_ongoing_games():
    await asyncio.sleep(5)
    games = client.games.get_ongoing()
    print(f"There are currently {len(games)} games ongoing.")
    return games


async def stream_game(game_id):
    stream = client.bots.stream_game_state(game_id)
    for event in stream:
        return(event)

    
async def loop_games():
    '''
    Loop through all current games and act on them
    '''
    while True:
        games = await get_ongoing_games()
        game_ids = [game["gameId"] for game in games]
        for game_id in game_ids:
            event = await stream_game(game_id)
            print(event)

loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(loop_games())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Ending asyncio loop")
    loop.close()