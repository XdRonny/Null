import os
import wget
import asyncio
import speedtest
from PIL import Image
from pyrogram.types import Message
from pyrogram import filters, Client
from DzL import app
from config import OWNER_ID

@app.on_message(filters.command("speedtest") & ~filters.edited)
async def run_speedtest(_, message):
    userid = message.from_user.id
    m = await message.reply_text("Running Speed test")
    test = speedtest.Speedtest()
    test.get_best_server()
    await m.edit("🔥 running download speedtest")
    test.download()
    await m.edit("🔥 running upload speedtest")
    test.upload()
    test.results.share()
    result = test.results.dict()
    await m.edit("💠 Sharing Speedtest")
    output = f"""💡 SpeedTest Results
    
<u>Client:</u>

ISP: {result['client']['isp']}
Country: {result['client']['country']}
  
<u>Server:</u>

Name: {result['server']['name']}
Country: {result['server']['country']}, {result['server']['cc']}
Sponsor: {result['server']['sponsor']}
Latency: {result['server']['latency']}  

⚡ Ping: {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()
