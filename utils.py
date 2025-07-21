import os
from datetime import datetime
import aiofiles

async def save_reply(tweet_url: str, reply: str):
    os.makedirs("output/replies", exist_ok=True)
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"output/replies/{now}.txt"
    async with aiofiles.open(filename, "w") as f:
        await f.write(f"TWEET: {tweet_url}\n\nREPLY:\n{reply}")
