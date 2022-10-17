# Credits <https://github.com/IndomieGorengSatu>
# @indomiegenetik

import random
import os

from pyrogram import filters
from DzL import userbot, app

@app.on_message(filters.command("cogan"))
async def asupan(client, message):
    y = await message.reply_text("**🔍 Mencari Cogan...**")
    try:
        asupannya = []
        async for asupan in userbot.one.search_messages("suchdiary", filter="photo"):
            asupannya.append(asupan)

        file=random.choice(asupannya)
        oh = await userbot.one.download_media(file)
        await app.send_photo(
            message.chat.id,
            oh,
            caption=f"**Ni cogan nya Kak {message.from_user.mention} 🥵**",
            )
        await y.delete()
    except Exception:
        await y.edit("**Gagal mencari cogan, lagi badmood...**")
    os.remove(oh)


@app.on_message(filters.command("cecan"))
async def asupan(client, message):
    y = await message.reply_text("**🔍 Mencari Cecan...**")
    try:
        asupannya = []
        async for asupan in userbot.one.search_messages("kiddrugs", filter="photo"):
            asupannya.append(asupan)

        file=random.choice(asupannya)
        oh = await userbot.one.download_media(file)
        await app.send_photo(
            message.chat.id,
            oh,
            caption=f"**Ni cecan nya kak {message.from_user.mention} 🤗**",
            )
        await y.delete()
    except Exception:
        await y.edit("**Gagal mencari cecan, lagi badmood...**")
    os.remove(oh)


@app.on_message(filters.command("wibu"))
async def asupan(client, message):
    y = await message.reply_text("**🔍 Mencari Gambar Wibu...**")
    try:
        asupannya = []
        async for asupan in userbot.one.search_messages("ppcpanime", filter="photo"):
            asupannya.append(asupan)

        file=random.choice(asupannya)
        oh = await userbot.one.download_media(file)
        await app.send_photo(
            message.chat.id,
            oh,
            caption=f"**Ni {message.from_user.mention} gambar wibu nya, dasar wibu😆**",
            )
        await y.delete()
    except Exception:
        await y.edit("**Gagal mencari gambar wibu, lagi badmood..**")
    os.remove(oh)
