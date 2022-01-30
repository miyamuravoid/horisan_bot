import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from horisan.events import register as MEMEK
from horisan import telethn as tbot

PHOTO = "https://telegra.ph/file/9e95d6f3e8eeaa4ae4ea8.mp4"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  horisan = "**HI BAKA IM HORI SAN!** \n\n"
  horisan += "×**I'm Working well managed** \n\n"
  horisan += "×**My Owners : [VOID](https://t.me/voidxtoxic)"
  horisan += f"×**Telethon Version : {tlhver}** \n\n"
  horisan += f"×**Pyrogram Version : {pyrover}** \n\n"
  horisan += "**Thanks For Adding Me Here Baka ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/YumekoProBot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/horisanbotsupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=horisan,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  horisan = "✅ **bot restarted successfully**\n\n• Admin list has been **reloaded**"
  BUTTON = [[Button.url("📡 ᴜᴘᴅᴀᴛᴇs", "https://t.me/horisanbotsupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=horisan,  buttons=BUTTON)