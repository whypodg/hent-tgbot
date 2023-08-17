import asyncio
import datetime
import logging

import pyrogram
import pyrogram_patch
from pyrogram import filters, types
from pyrogram_patch.router import Router

import utils
from utils import keyboards as kbs


other = Router()
other.name = "other"


@other.on_message(
	filters.command(commands=["start", "commands", "help", "menu", "старт", "команды", "помощь", "меню"], prefixes=["/", "!"])
)
async def start(client: pyrogram.Client, message: types.Message):
	out = f"📃 <b>Справка по использованию <a href='tg://user?id={utils.config['id']}'>Hentai Bot 🌚</a>.</b>" \
		  f"\nПри наличии вопросов можно обратиться в чат помощи с ботом или к <a href='tg://user?id={utils.config['dev_id']}'>" \
		  f"разработчику</a>.\n\nЕсли кнопки не работают, или не открываются ссылки:" \
		  f"\n  • 📝 <b>Список команд:</b> teletype.in/@whypodg/hent-cmd" \
		  f"\n  • 💬 <b>Чат:</b> @henttgchat" \
		  f"\n  • ➕ <b><a href='https://t.me/henttgbot?startgroup=start'>Добавить бота в чат</a></b>"

	await utils.answer(
		message, out,
		disable_notification=True,
		reply_markup=kbs.kb_help
	)


@other.on_message(
	filters.command(commands=["ping", "пинг"], prefixes=["/", "!"])
)
async def ping(client: pyrogram.Client, message: types.Message):
	ev = (datetime.datetime.now() - message.date).microseconds / 1000
	s = datetime.datetime.now()
	msg = await utils.answer(
		message, "🌘"
	)
	e = round((datetime.datetime.now()-s).microseconds/1000, 2)

	sapi = datetime.datetime.now()
	await client.get_chat(message.chat.id)
	eapi = round((datetime.datetime.now()-sapi).microseconds/1000, 2)

	await utils.edit(
		msg, f"⚙ <b>Понг!</b>\n<b>Event latency: {int(ev)}ms | Handler took: {e}ms | API: {eapi}ms</b>",
		reply_markup=kbs.kb_ping
	)


@other.on_callback_query(filters.regex("ping"))
async def pingCB(client: pyrogram.Client, query: types.CallbackQuery):
	s = datetime.datetime.now()
	msg = await utils.edit(
		query.message, "🌘"
	)
	ev = (datetime.datetime.now() - msg.date).microseconds / 1000
	e = round((datetime.datetime.now()-s).microseconds/1000, 2)

	sapi = datetime.datetime.now()
	await client.get_chat(msg.chat.id)
	eapi = round((datetime.datetime.now()-sapi).microseconds/1000, 2)

	await utils.edit(
		msg, f"⚙ <b>Понг!</b>\n<b>Event latency: {int(ev)}ms | Handler took: {e}ms | API: {eapi}ms</b>",
		reply_markup=kbs.kb_ping
	)