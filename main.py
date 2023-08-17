import logging
import os

import pyrogram
import pyrogram_patch
#from pyrogram_patch.router import Router

import utils
from commands import routers
from utils.middleware import RegUser

logging.basicConfig(
	level=logging.DEBUG,
	format='[%(asctime)s] [%(levelname)s] [%(name)s.%(funcName)s:%(lineno)d]\n>>> %(message)s',
	filename='logs.log',
	filemode='w+'
)

client = pyrogram.Client(
	name="hentaiBot",
	api_id=utils.config['app']['id'],
	api_hash=utils.config['app']['hash'],
	app_version=f"HentaiBot v{utils.config['version']}",
	bot_token=utils.config['token'],
	parse_mode=pyrogram.enums.ParseMode.HTML
)
patch = pyrogram_patch.patch(client)


os.system("clear")
print("\033[34mИнформация по роутерам:\033[0m")
for router in routers:
	if utils.config['commands'][router.name]:
		patch.include_router(router)
		print(f"\033[32m  • Роутер [{router.name}] успешно добавлен!\033[0m")
		continue
	print(f"\033[31m  • Роутер [{router.name}] отключен.\033[0m")


print(f"\033[34mБот [Hentai TG Bot] успешно запущен!\033[0m")
patch.include_middleware(RegUser())
client.run()