# import logging
# import logging.config

# # Get logging configurations
# logging.config.fileConfig('logging.conf')
# logging.getLogger().setLevel(logging.INFO)
# logging.getLogger("pyrogram").setLevel(logging.ERROR)
# logging.getLogger("imdbpy").setLevel(logging.ERROR)




from pyrogram import Client, __version__
# from pyrogram.raw.all import layer
# from database.ia_filterdb import Media
# from database.users_chats_db import db
# #from info import SESSION, API_ID, API_HASH, BOT_TOKEN, LOG_STR, LOG_CHANNEL, PORT
# from info import *
from utils import temp
# from typing import Union, Optional, AsyncGenerator
# from pyrogram import types
# from Script import script 
# from datetime import date, datetime 
# import pytz
# from aiohttp import web
# from plugins import web_server

#async def start_services():
class Bot(Client):


   def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

   async def start(self):
        b_users, b_chats = await db.get_banned()
        temp.BANNED_USERS = b_users
        temp.BANNED_CHATS = b_chats
        await super().start()
        await Media.ensure_indexes()
        me = await self.get_me()
        temp.ME = me.id
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        self.username = '@' + me.username
        logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
        logging.info(LOG_STR)
        logging.info(script.LOGO)
        tz = pytz.timezone('Asia/Kolkata')
        today = date.today()
        now = datetime.now(tz)
        time = now.strftime("%H:%M:%S %p")
        await self.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(today, time))
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

#     async def stop(self, *args):
#         await super().stop()
#         logging.info("Bot stopped. Bye.")

#     async def iter_messages(
#         self,
#         chat_id: Union[int, str],
#         limit: int,
#         offset: int = 0,
#     ) -> Optional[AsyncGenerator["types.Message", None]]:
#         """Iterate through a chat sequentially.
#         This convenience method does the same as repeatedly calling :meth:`~pyrogram.Client.get_messages` in a loop, thus saving
#         you from the hassle of setting up boilerplate code. It is useful for getting the whole chat messages with a
#         single call.
#         Parameters:
#             chat_id (``int`` | ``str``):
#                 Unique identifier (int) or username (str) of the target chat.
#                 For your personal cloud (Saved Messages) you can simply use "me" or "self".
#                 For a contact that exists in your Telegram address book you can use his phone number (str).
                
#             limit (``int``):
#                 Identifier of the last message to be returned.
                
#             offset (``int``, *optional*):
#                 Identifier of the first message to be returned.
#                 Defaults to 0.
#         Returns:
#             ``Generator``: A generator yielding :obj:`~pyrogram.types.Message` objects.
#         Example:
#             .. code-block:: python
#                 for message in app.iter_messages("pyrogram", 1, 15000):
#                     print(message.text)
#         """
#         current = offset
#         while True:
#             new_diff = min(200, limit - current)
#             if new_diff <= 0:
#                 return
#             messages = await self.get_messages(chat_id, list(range(current, current+new_diff+1)))
#             for message in messages:
#                 yield message
#                 current += 1


# app = Bot()
# app.run()
import logging
import logging.config
# Credit @LazyDeveloper.
# Please Don't remove credit.
# Born to make history @LazyDeveloper !
# Thank you LazyDeveloper for helping us in this Journey
# 🥰  Thank you for giving me credit @LazyDeveloperr  🥰
# for any error please contact me -> telegram@LazyDeveloperr or insta @LazyDeveloperr 
# rip paid developers 🤣 - >> No need to buy paid source code while @LazyDeveloperr is here 😍😍
# Get logging configurations
#########duplicate###########
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from database.ia_filterdb import Media
from database.users_chats_db import db
#from info import SESSION, API_ID, API_HASH, BOT_TOKEN, LOG_STR, LOG_CHANNEL, PORT
from info import *
from utils import temp
from typing import Union, Optional, AsyncGenerator
from pyrogram import types
from Script import script 
from datetime import date, datetime 
import pytz
from aiohttp import web
from plugins import web_server
#########duplicate###########


import sys
import glob
import importlib
from pathlib import Path
from pyrogram import idle
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

from pyrogram import __version__
from info import *

from aiohttp import web
from plugins import web_server

import asyncio
from pyrogram import idle
from lazybot import LazyPrincessBot
from util.keepalive import ping_server
from lazybot.clients import initialize_clients


ppath = "plugins/*.py"
files = glob.glob(ppath)
LazyPrincessBot.start()
loop = asyncio.get_event_loop()


async def start_services():
    print('\n')
    print('------------------- Initalizing Telegram Bot -------------------')
    bot_info = await LazyPrincessBot.get_me()
    LazyPrincessBot.username = bot_info.username
    print("------------------------------ DONE ------------------------------")
    print()
    print(
        "---------------------- Initializing Clients ----------------------"
    )
    await initialize_clients()
    print("------------------------------ DONE ------------------------------")
    print('\n')
    print('--------------------------- Importing ---------------------------')
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem.replace(".py", "")
            plugins_dir = Path(f"plugins/{plugin_name}.py")
            import_path = "plugins.{}".format(plugin_name)
            spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
            load = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(load)
            sys.modules["plugins." + plugin_name] = load
            print("Imported => " + plugin_name)
    if ON_HEROKU:
        print("------------------ Starting Keep Alive Service ------------------")
        print()
        asyncio.create_task(ping_server())
    print('-------------------- Initalizing Web Server -------------------------')
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0" if ON_HEROKU else BIND_ADRESS
    await web.TCPSite(app, bind_address, PORT).start()
    print('----------------------------- DONE ---------------------------------------------------------------------')
    print('\n')
    print('---------------------------------------------------------------------------------------------------------')
    print('---------------------------------------------------------------------------------------------------------')
    print('\n')
    print('----------------------- Service Started -----------------------------------------------------------------')
    print('                        bot =>> {}'.format((await LazyPrincessBot.get_me()).first_name))
    print('                        server ip =>> {}:{}'.format(bind_address, PORT))
    if ON_HEROKU:
        print('                        app runnng on =>> {}'.format(FQDN))
    print('---------------------------------------------------------------------------------------------------------')
    print('---------------------------------------------------------------------------------------------------------')
    await idle()

if __name__ == '__main__':
    try:
        loop.run_until_complete(start_services())
    except KeyboardInterrupt:
        logging.info('----------------------- Service Stopped -----------------------')

