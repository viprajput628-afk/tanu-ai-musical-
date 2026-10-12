
import os
from pyrogram import Client, filters

app = Client(
    "vplay_bot",
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
    bot_token=os.environ["BOT_TOKEN"],
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("VPlay Bot online hai! 🎵")

@app.on_message(filters.command("ping"))
async def ping(client, message):
    await message.reply_text("Bot working hai! ✅")

print("Bot starting...")
app.run()
