import asyncio
import datetime
import logging
import os
import sys
from meval import meval

import pyrogram
import pyrogram_patch
from pyrogram import filters, types
from pyrogram_patch.router import Router

import utils
from dispatch import filters as custom_filters


admin = Router()
admin.name = "admin"

async def getattrs(client, message):
	return {**{
		"utils": utils,
		"db": utils.db,
		"config": utils.config,
		"bot": client,
		"client": client,
		"c": client,
		"message": message,
		"m": message,
		"reply": message.reply_to_message,
		"r": message.reply_to_message
	}}


@admin.on_message(
	filters.command(commands=["eval", "e", "евал", "ебал", "е"], prefixes=["/", "!"])
	& filters.user(utils.getUsersStatus(5))
)
async def eval(client: pyrogram.Client, message: types.Message):
	args = utils.get_raw_args(message)

	try:
		result = await meval(
			args,
			globals(),
			**await getattrs(client, message),
		)
	except Exception:
		await utils.answer(
			message,
			f"💻 <b>Код:</b>\n<code>{args}</code>\n\n❌ <b>Ошибка</b>:\n<code>{sys.exc_info()}</code>"
		)

	if result:
		result = str(result)
		result = result.replace(
			utils.config['token'],
			"*"*len(utils.config['token'])
		)
		result = result.replace(
			str(utils.config['app']['id']),
			"*"*len(str(utils.config['app']['id']))
		)
		result = result.replace(
			utils.config['app']['hash'],
			"*"*len(utils.config['app']['hash'])
		)
	await utils.answer(
		message,
		f"💻 <b>Код:</b>\n<code>{args}</code>\n\n✅ <b>Результат:</b>\n<code>{result}</code>"
	)


@admin.on_message(
	filters.command(commands=["terminal", "t", "терминал"], prefixes=["/", "!"])
	& filters.user(utils.getUsersStatus(5))
)
async def eval(client: pyrogram.Client, message: types.Message):
	args = utils.get_raw_args(message)

	out, err = await (await asyncio.create_subprocess_shell(
		args,
		stdout=asyncio.subprocess.PIPE,
		stderr=asyncio.subprocess.PIPE,
		cwd=os.path.abspath(os.path.dirname(os.path.abspath("main.py")))
	)).communicate()

	await utils.answer(
		message,
		f"⌨️ <b>Системная команда</b> <code>{args}</code>\n📼 <b>Вывод:</b> <code>{out.decode()}</code>" + (f"\n\n❌ <b>Ошибки:</b>\n{err.decode()}" if err.decode() != "" else "")
	)