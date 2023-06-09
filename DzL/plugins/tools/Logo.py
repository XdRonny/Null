import os 
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
from pyrogram import filters
from DzL import app
from pyrogram import Client as bot

app.on_message(filters.command('logo'))
async def makelogo(event):
        quew = event.pattern_match.group(1).strip()
            
        if not quew:
           await event.reply('Provide Some Text To Draw! Example: /logo <your name>')
           return
        else:
           pass
        msg = await event.reply('Creating your logo...wait!')
        try:
            text = quew
            if ";" in text:
                upper_text, lower_text = text.split(";")
                upper_text = upper_text.strip() 
                lower_text = lower_text.strip()
            else:
               upper_text = text
               lower_text = ""
            
            bg = [ 

               "https://telegra.ph/file/c08cd6b8a0819d5a0c32b.jpg",

               "https://telegra.ph/file/78365f4c13507fafdadff.jpg",

               "https://telegra.ph/file/d0d3b3e43b24d57c1eb3d.jpg",

               "https://telegra.ph/file/b9a025cce1d58bc6365a8.jpg",

               "https://telegra.ph/file/35686259565dbd5ec2765.jpg",

               "https://telegra.ph/file/a67131ccce82e499d1a37.jpg",

               "https://telegra.ph/file/1eeee3354ad14f6ba3fcc.jpg",

               "https://telegra.ph/file/5d4b16821fcb779dd02a9.jpg",

               "https://telegra.ph/file/8b1d9a4ecf06a6bafa114.jpg",

               "https://telegra.ph/file/5bfc583000e4ecd8bce36.jpg",

               "https://telegra.ph/file/924d69f508ba1d67fd4d5.jpg",

               "https://telegra.ph/file/6b88f57147abfcf543d21.jpg",

               "https://telegra.ph/file/806b472f3c2dedc131734.jpg",

               "https://telegra.ph/file/2badb1bcc636d00af70b9.jpg",

               "https://telegra.ph/file/ed6806a4ba310008a96a5.jpg",

               "https://telegra.ph/file/99eb170e579e7b7f2fbc8.jpg",

               "https://telegra.ph/file/12218896d755952806e4b.jpg",

               "https://telegra.ph/file/2bfe013c59efa1d40aaf1.jpg",

               "https://telegra.ph/file/84d3872334efcba960de6.jpg",

               "https://telegra.ph/file/f24182fab85e732f7b8a2.jpg",

               "https://telegra.ph/file/da1f931a438986834d464.jpg",

               "https://telegra.ph/file/d3bdda4ea1cbeb03d338e.jpg",

               "https://telegra.ph/file/1028be52628cabf7d9c14.jpg",

               "https://telegra.ph/file/aee7df75a5edd1b02abde.jpg",

               "https://telegra.ph/file/98594f777a3ff7ca56590.jpg",

               "https://telegra.ph/file/59452682abf194ba52f35.jpg",

               "https://telegra.ph/file/be93f3a8f47ddc06595da.jpg",

               "https://telegra.ph/file/4b4332ad51927956ec162.jpg",

               "https://telegra.ph/file/65ed566139a6f59330635.jpg",

               "https://telegra.ph/file/6fdaf704c340fd90b7447.jpg",

               "https://telegra.ph/file/bcf8802314be0877f52c1.jpg",

               "https://telegra.ph/file/1117b9082db928a8ac715.jpg",

               "https://telegra.ph/file/73066d5a889acb8584c9a.jpg",

               "https://telegra.ph/file/a4b2724f0093a02eb5b21.jpg",

               "https://telegra.ph/file/b441ce7cbcd42a504c26c.jpg",

               "https://telegra.ph/file/015ee9a1f298172057927.jpg",

               "https://telegra.ph/file/13a931844555d6c81607e.jpg",

               "https://telegra.ph/file/0b064018f9f215bfe80e7.jpg",

               "https://telegra.ph/file/a94997aed961538c1e337.jpg",

               "https://telegra.ph/file/9306426c58e6e7023f8e1.jpg",

               "https://telegra.ph/file/eef9b1c624ede2e1fc228.jpg",

               "https://telegra.ph/file/9104a1cc8b5723127eb53.jpg",

               "https://telegra.ph/file/f5165e56fea4b88147a92.jpg",

               "https://telegra.ph/file/410adb4ec98240d30a5c4.jpg",

               "https://telegra.ph/file/7875ff3e14eaec152fb2a.jpg",

               "https://telegra.ph/file/e8bc77680f372fdc72500.jpg",

               "https://telegra.ph/file/549ee1b63dfe591407a3b.jpg",

               "https://telegra.ph/file/db60ae3dc5c40c76d17a8.jpg",

               "https://telegra.ph/file/78b19ab4ee0818e656fd1.jpg",

               "https://telegra.ph/file/df38634a97049002eedc0.jpg",

               "https://telegra.ph/file/61f6de393faaaa8b3daf6.jpg",

               "https://telegra.ph/file/494ceb487fc918fee564b.jpg",

               "https://telegra.ph/file/25815bf5d1700c6a4d1ea.jpg",

               "https://telegra.ph/file/df4d965a205a7e6a3e6d7.jpg",

               "https://telegra.ph/file/760635adfcb05cbe336d6.jpg",

               "https://telegra.ph/file/86d2be2aa379bc9077c97.jpg",

               "https://telegra.ph/file/facce3eed4cc3a60a145d.jpg",

               "https://telegra.ph/file/550aa046ab930967bc377.jpg",

               "https://telegra.ph/file/7c1696bc94225779d656a.jpg",

            ]
            
            randBg = random.choice(bg)
            

            allFonts = [
            "font(1).otf", "font(2).otf", "font(3).otf", "font(4).otf","font(5).otf","font(6).otf", "font(7).otf", "font(8).otf",
            "font(9).otf", "font(10).otf", "font(11).otf","font(12).otf", "font(13).otf", "font(14).otf", "font(15).otf", "font(16).otf",
            "font(17).otf", "font(18).otf",
            "tfont(1).ttf", "tfont(2).ttf", "tfont(3).ttf", "tfont(4).ttf", "tfont(5).ttf","tfont(6).ttf", "tfont(7).ttf", "tfont(8).ttf",
            "tfont(9).ttf", "tfont(10).ttf", "tfont(11).ttf", "tfont(12).ttf", "tfont(13).ttf","tfont(14).ttf", "tfont(15).ttf", "tfont(16).ttf",
            "tfont(17).ttf", "tfont(18).ttf", "tfont(19).ttf", "tfont(20).ttf", "tfont(21).ttf", "tfont(22).ttf", "tfont(23).ttf", "tfont(24).ttf",
            "tfont(25).ttf", "tfont(26).ttf", "tfont(27).ttf", "tfont(28).ttf", "tfont(29).ttf", "tfont(30).ttf", "tfont(31).ttf", "tfont(32).ttf",
            "tfont(33).ttf", "tfont(34).ttf", "tfont(35).ttf", "tfont(36).ttf","tfont(37).ttf", "tfont(38).ttf", "tfont(39).ttf", "tfont(40).ttf",
            "tfont(41).ttf", "tfont(42).ttf",  
            ]
            randFont = random.choice(allFonts)
            response = requests.get(randBg)
            img = Image.open(BytesIO(response.content))
            blueimg = img.filter(ImageFilter.BoxBlur(1))
            draw = ImageDraw.Draw(blueimg)
            imgSize = blueimg.size


            if upper_text:
        
                  
                  fontSize = int(imgSize[1] / 5)
                  image_widthz, image_heightz = img.size    
                  font = ImageFont.truetype(f"./AliciaRobot/resources/fonts/{randFont}", fontSize)
                  textSize = font.getsize(upper_text)
                  while textSize[0] > imgSize[0] - 100:
                     fontSize -= 1
                     font = ImageFont.truetype(f"./AliciaRobot/resources/fonts/{randFont}", fontSize)
                     textSize = font.getsize(upper_text)
                  w, h = draw.textsize(upper_text, font=font)
                  h += int(h*0.5)
                  image_width, image_height = blueimg.size
                  x = (image_widthz-w)/2
                  y= ((image_heightz-h)/1.9+6)
                  draw.text((x, y), upper_text, font=font, fill="white", stroke_width=1, stroke_fill="black")
        
                  
              
            if lower_text:
        
                  fontSize = int(imgSize[1] / 14)
                  image_widthz, image_heightz = img.size
                  font = ImageFont.truetype(f"./AliciaRobot/resources/fonts/{randFont}", fontSize)
                  textSize = font.getsize(lower_text)
                  while textSize[0] > imgSize[0] - 100:
                     fontSize -= 1
                     font = ImageFont.truetype(f"./AliciaRobot/resources/fonts/{randFont}", fontSize)
                     textSize = font.getsize(lower_text)
                  w, h = draw.textsize(lower_text, font=font)
                  h += int(h*0.5)
                  image_width, image_height = blueimg.size
                  x = (image_widthz-w)/2
                  y= ((image_heightz-h)/1.6+6)
                  
                  draw.text((x, y), lower_text, font=font, fill="white", stroke_width=2, stroke_fill="black")
                  
            fname2 = "logobycoder.png"
            blueimg.save(fname2, "png")
            await bot.send_file(event.chat_id, fname2, caption="Made By @TGN_Ro_bot")
            if os.path.exists(fname2):
               os.remove(fname2)
    

        except Exception as e:
            await msg.edit(f"Please Try Again! \nif you're getting Error again and again then Report @GodfatherSupport")
