# Credits <https://github.com/IndomieGorengSatu>
# @indomiegenetik

import random
import os

from pyrogram import filters
from DzL import userbot, app

@app.on_message(filters.command("estetik"))
async def asupan(client, message):
    y = await message.reply_text("**🔍 Mencari Gambar Estetiknya...**")
    try:
        asupannya = []
        async for asupan in userbot.one.search_messages("aesthetic_gambar", filter="photo"):
            asupannya.append(asupan)

        file=random.choice(asupannya)
        oh = await userbot.one.download_media(file)
        await app.send_photo(
            message.chat.id,
            oh,
            caption=f"**Ni Kak {message.from_user.mention}, estoktok bukan🙌✨**",
            )
        await y.delete()
    except Exception:
        await y.edit("**Gagal mencari, lagi badmood**")
    os.remove(oh)


@app.on_message(filters.command("ayang"))
async def asupan(client, message):
    y = await message.reply_text("**🔍 Mencari Ayang nya {message.from_user.mention}...**")
    try:
        asupannya = []
        async for asupan in userbot.one.search_messages("IndomieGantengV2", filter="photo"):
            asupannya.append(asupan)

        file=random.choice(asupannya)
        oh = await userbot.one.download_media(file)
        await app.send_photo(
            message.chat.id,
            oh,
            caption=f"**Ni Ayangnya {message.from_user.mention} 🥰❤️🤪**",
            )
        await y.delete()
    except Exception:
        await y.edit("**Gada yg mau sama u, minimal ganteng la...😆**")
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
        await y.edit("**Gagal mencari, lagi badmood**")
    os.remove(oh)
