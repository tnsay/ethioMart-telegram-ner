# Telegram scraper script placeholder

# client = TelegramClient('session', api_id, api_hash)
# await client.start()

# channel = await client.get_entity('https://t.me/shageronlinestore')
# messages = await client.get_messages(channel, limit=1000)
from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto
import os, json
from config import api_id, api_hash

# Session setup
client = TelegramClient('ethioMartSession', api_id, api_hash)

channels = [
    "@marakibrand",
    "@classybrands",
    "@meneshayeofficial",
    "@forfreemarket",
    "@ZemenExpress"
]

# Directories
image_dir = "images"
output_dir = "data/raw"
os.makedirs(image_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)


async def scrape_channel(channel_username, limit=200):
    await client.start()
    messages_data = []
    async for message in client.iter_messages(channel_username, limit=limit):
        if message.message:
            msg = {
                "channel": channel_username,
                "date": str(message.date),
                "message": message.message,
                "views": message.views,
                "id": message.id
            }

            # Download image if available
            if message.media and isinstance(message.media, MessageMediaPhoto):
                image_path = os.path.join(image_dir, f"{channel_username[1:]}_{message.id}.jpg")
                await client.download_media(message, file=image_path)
                msg["image"] = image_path

            messages_data.append(msg)

    # Save JSON output
    file_name = f"{channel_username[1:]}.json"
    with open(os.path.join(output_dir, file_name), "w", encoding="utf-8") as f:
        json.dump(messages_data, f, ensure_ascii=False, indent=4)
    print(f"✅ Done scraping {channel_username}, saved {len(messages_data)} messages.")

# Run the scraping loop
with client:
    for channel in channels:
        client.loop.run_until_complete(scrape_channel(channel))