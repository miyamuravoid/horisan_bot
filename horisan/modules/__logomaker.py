import os
import io
import requests
import shutil 
import random
import re
import glob
import time

from io import BytesIO
from requests import get
from telethon.tl.types import InputMessagesFilterPhotos

from horisan import OWNER_ID, BOT_USERNAME, SUPPORT_CHAT
from horisan.events import register
from horisan import telethn
from PIL import Image, ImageDraw, ImageFont


LOGO_LINKS            = ["https://telegra.ph/file/de27676f4c78355f0b558.jpg",
"https://telegra.ph/file/cfdd37ebc593afdfdc355.jpg",
"https://telegra.ph/file/c0de26bf15d8722fd14a6.jpg",
"https://telegra.ph/file/a8307a2aed0cf21cc8ef8.jpg",
"https://telegra.ph/file/6f888febe234ab179e89f.jpg",
"https://telegra.ph/file/e7898e0c265a045441e2f.jpg",
"https://telegra.ph/file/4ddec01c9eb49630c77e5.jpg",
"https://telegra.ph/file/02d7536a5702da8809c5b.jpg",
"https://telegra.ph/file/62e13d4c7f4173530478b.jpg",
"https://telegra.ph/file/17f13bdd3b5adbc6931de.jpg",
"https://telegra.ph/file/48678096c04084b228fa0.jpg",
"https://telegra.ph/file/8ea44ce4d311e010f8b38.jpg",
"https://telegra.ph/file/603841451f84efaa710c8.jpg",
"https://telegra.ph/file/04f1920bd07f56dc592b3.jpg"
                         ]

@register(pattern="^/logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id != OWNER_ID and not quew:
  await event.reply('`Please give me the text for the logo!`\n`Example /logo <pantek>`')
  return
 pesan = await event.reply('`Creating your logo...`')
 try:
    text = event.pattern_match.group(1)
    randc = random.choice(LOGO_LINKS)
    img = Image.open(io.BytesIO(requests.get(randc).content))
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "black"
    shadowcolor = "blue"
    fnt = glob.glob("./lunaBot/logopom/*")
    randf = random.choice(fnt)
    font = ImageFont.truetype(randf, 120)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y = ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=1, stroke_fill="black")
    fname = "luna.png"
    img.save(fname, "png")
    await telethn.send_file(event.chat_id, file=fname, caption = f"Made by [Luna ✨](https://t.me/lunatapibot)")         
    await pesan.delete()
    if os.path.exists(fname):
            os.remove(fname)
 except Exception as e:
    await event.reply(f'Error, Report @lunaXresso')