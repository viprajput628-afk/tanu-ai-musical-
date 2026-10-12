
import os
import pyrogram.errors
from pyrogram import Client, filters

try:
    if not hasattr(pyrogram.errors, "GroupcallForbidden"):
        pyrogram.errors.GroupcallForbidden = (
            pyrogram.errors.GroupCallForbidden
        )
except AttributeError:
    class GroupcallForbidden(Exception):
        pass

    pyrogram.errors.GroupcallForbidden = GroupcallForbidden

from pytgcalls import PyTgCalls

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
BOT_TOKEN = os.environ["BOT_TOKEN"]
SESSION_STRING = os.environ["SESSION_STRING"]

bot = Client(
    "vplay_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

user = Client(
    "vplay_user",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING
)

calls = PyTgCalls(user)

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "🎵 VPlay Kesariya Music Bot\n"
        "Bot connected hai! 🎶"
    )

@bot.on_message(filters.command("play") & filters.group)
async def play_song(client, message):
    if len(message.command) < 2:
        await message.reply_text(
            "Gaane ka naam likho: /play song name"
        )
        return

    await message.reply_text(
        "🎵 Request mili. Music setup aur voice chat "
        "availability verify ki ja rahi hai."
    )

bot.run()
