import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from horisan.events import register as MEMEK
from horisan  import telethn as tbot

PHOTO = "https://telegra.ph/file/940b63c7bdc98386fcc9d.mp4"

@MEMEK(pattern=("/mhelp"))
async def awake(event):
  tai = event.sender.first_name
  horisan = "** ──「 Basic Guide 」── ** \n\n"
  horisan += "• /play **(song title) — To Play the song you requested via YouTube** \n"
  horisan += "• /search ** (song/video title) – To search for links on YouTube with details** \n"
  horisan += "• /playlist - **show the list song in queue** \n"
  horisan += "•/lyric - ** (song name) lyrics scrapper** \n\n"
  horisan += "** ──「 Admin CMD 」── ** \n\n"
  horisan += "• /pause - **To Pause Song playback** \n"
  horisan += "• /resume - **To resume playback of the paused Song** \n"
  horisan += "• /skip - **To Skip playback of the song to the next Song** \n"
  horisan += "• /end - **To Stop Song playback** \n"
  horisan += "• /control - **open the player settings panel** \n"
  horisan += "• /reload - **To Refresh admin list** \n"

  BUTTON = [[Button.url("☎️ Support", "https://t.me/horisanbotsupport"), Button.url("📡 Updates", "https://t.me/ZeinzoProject")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)