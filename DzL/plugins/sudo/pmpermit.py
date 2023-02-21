import asyncio
from pyrogram import Client
from config import PMPERMIT
from pyrogram import filters
from pyrogram.types import Message
from DzL import userbot as USER
from DzL.misc import SUDOERS as SUDO_USERS


PMSET =True
pchats = []


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(message.chat.id, f"**Hello, need something? dont pm here, im just assistant bot, not a human, so please send dm to my owner for any issues.\n\n📍 Owner: @justDzL\n📍 Channel: @suaradz\n\n")
            return

    
@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("✅ Pmpermit turned on")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("❌ Pmpermit turned off")
            return


@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("approved to pm due to outgoing messages")
        return
    message.continue_propagation()

 
@USER.on_message(filters.command("yes", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("✅ approved to pm.")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("no", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("❌ disapproved to pm.")
        return
    message.continue_propagation()
