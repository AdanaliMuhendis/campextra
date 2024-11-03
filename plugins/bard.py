import requests
from pyrogram import filters

from AlemMuzik import app
from SafoneAPI import SafoneAPI


@app.on_message(filters.command(["bard"]))
async def bard(bot, message):
    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply_text(
            "Örnek:\n\n`/bard bana lord rama ve sita'dan kısaca bahset`"
        )
        return

    if message.reply_to_message and message.reply_to_message.text:
        user_input = message.reply_to_message.text
    else:
        user_input = " ".join(message.command[1:])

    try:
        Z = await SafoneAPI().bard(user_input)
        result = Z["candidates"][0]["content"]["parts"][0]["text"]
        await message.reply_text(result)
    except requests.exceptions.RequestException as e:
        pass
