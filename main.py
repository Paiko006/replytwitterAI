import asyncio
from tweet_scraper import get_tweet_text
from gemini_reply import generate_reply
from utils import save_reply

async def main():
    with open("input/tweet_links.txt") as f:
        tweet_links = [line.strip() for line in f if line.strip()]

    for link in tweet_links:
        print(f"📥 Memproses: {link}")
        tweet_text = get_tweet_text(link)
        if not tweet_text:
            print("⚠️ Gagal ambil tweet.")
            continue
        reply = await generate_reply(tweet_text)
        await save_reply(link, reply)
        print("✅ Disimpan!\n")

if __name__ == "__main__":
    asyncio.run(main())
