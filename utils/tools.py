import html
import json
import re
import typing

import pyrogram
from pyrogram import types

from db import DataBase

config = json.loads(open("config.json", "r", encoding="utf-8").read())
db = DataBase()


def pluralForm(count, variants):
	count = abs(count)
	if count % 10 == 1 and count % 100 != 11:
		var = 0
	elif 2 <= count % 10 <= 4 and (count % 100 < 10 or count % 100 >= 20):
		var = 1
	else:
		var = 2
	return f"{count} {variants[var]}"


def get_args(message):
	text = message.text
	text = text.split(maxsplit=1)[1:]
	if len(text) == 0:
		return []
	return text[0].split()


def get_raw_args(message):
	text = message.text
	text = text.split(maxsplit=1)[1:]
	if len(text) == 0:
		return ""
	return text[0]


def getUsersStatus(status: int) -> list:
	us = db.recvs(f"SELECT * FROM users WHERE status >= {status}")
	return [i[0] for i in us]


async def answer(
	message: types.Message,
	response: str,
	reply: bool = True,
	chat_id: int = 0,
	**kwargs
) -> typing.Union[types.Message, typing.List]:
	if isinstance(message, list) and message:
		message = message[0]
	text = parseText(html.escape(response))

	if len(text) > 4096:
		msgs = []
		for x in range(0, len(text), 4096):
			msgs.append(await message._client.send_message(
				chat_id=message.chat.id if chat_id == 0 else chat_id,
				text=text[x:x+4096],
				reply_to_message_id=message.id if reply else None,
				**kwargs
			))
		return msgs
	else:
		return await message._client.send_message(
			chat_id=message.chat.id if chat_id == 0 else chat_id,
			text=text,
			reply_to_message_id=message.id if reply else None,
			**kwargs
		)


async def edit(
	message: types.Message,
	response: str,
	id: int = 0,
	chat_id: int = 0,
	**kwargs
) -> types.Message:
	if isinstance(message, list) and message:
		message = message[0]
	text = parseText(html.escape(response))

	return await message._client.edit_message_text(
		chat_id=message.chat.id if chat_id == 0 else chat_id,
		message_id=message.id if id == 0 else id,
		text=text,
		**kwargs
	)


async def answer_photo(
	message: types.Message,
	photo: typing.Union[str, typing.BinaryIO],
	caption: str = None,
	reply: bool = True,
	chat_id: int = 0,
	**kwargs
) -> typing.Union[types.Message, typing.List]:
	if isinstance(message, list) and message:
		message = message[0]

	text = parseText(html.escape(caption)) if caption else ""

	if len(text) > 1024:
		msgs = []
		for x in range(0, len(text), 1024):
			if x == 0:
				msgs.append(await message._client.send_photo(
					chat_id=message.chat.id if chat_id == 0 else chat_id,
					photo=photo,
					caption=text[x:x+1024],
					reply_to_message_id=message.id if reply else None,
					**kwargs
				))
			else:
				msgs.append(await message._client.send_message(
					chat_id=message.chat.id if chat_id == 0 else chat_id,
					text=text[x:x+1024],
					reply_to_message_id=message.id if reply else None,
					**kwargs
				))
		return msgs
	else:
		return await message._client.send_photo(
			chat_id=message.chat.id if chat_id == 0 else chat_id,
			photo=photo,
			caption=text,
			reply_to_message_id=message.id if reply else None,
			**kwargs
		)


async def answer_anim(
	message: types.Message,
	animation: typing.Union[str, typing.BinaryIO],
	caption: str = None,
	reply: bool = True,
	chat_id: int = 0,
	**kwargs
) -> typing.Union[types.Message, typing.List]:
	if isinstance(message, list) and message:
		message = message[0]

	text = parseText(html.escape(caption)) if caption else ""

	if len(text) > 1024:
		msgs = []
		for x in range(0, len(text), 1024):
			if x == 0:
				msgs.append(await message._client.send_animation(
					chat_id=message.chat.id if chat_id == 0 else chat_id,
					animation=animation,
					caption=text[x:x+1024],
					reply_to_message_id=message.id if reply else None,
					**kwargs
				))
			else:
				msgs.append(await message._client.send_message(
					chat_id=message.chat.id if chat_id == 0 else chat_id,
					text=text[x:x+1024],
					reply_to_message_id=message.id if reply else None,
					**kwargs
				))
		return msgs
	else:
		return await message._client.send_animation(
			chat_id=message.chat.id if chat_id == 0 else chat_id,
			animation=animation,
			caption=text,
			reply_to_message_id=message.id if reply else None,
			**kwargs
		)


async def edit_media(
	message: types.Message,
	media: types.InputMedia,
	id: int = 0,
	chat_id: int = 0,
	**kwargs
) -> typing.Union[types.Message, typing.List]:
	if isinstance(message, list) and message:
		message = message[0]

	return await message._client.edit_message_media(
		chat_id=message.chat.id if chat_id == 0 else chat_id,
		message_id=message.id if id == 0 else id,
		media=media,
		**kwargs
	)


def parseText(text: str) -> str:
	# yeah, shitcode...
	text = text.replace("&quot;", '"')
	text = text.replace("&#x27;", "'")
	text = text.replace("&lt;b&gt;", "<b>")
	text = text.replace("&lt;/b&gt;", "</b>")
	text = text.replace("&lt;i&gt;", "<i>")
	text = text.replace("&lt;/i&gt;", "</i>")
	text = text.replace("&lt;tg-spoiler&gt;", "<tg-spoiler>")
	text = text.replace("&lt;/tg-spoiler&gt;", "</tg-spoiler>")
	text = text.replace("&lt;code&gt;", "<code>")
	text = text.replace("&lt;/code&gt;", "</code>")
	text = text.replace("&lt;pre&gt;", "<code>")
	text = text.replace("&lt;/pre&gt;", "</code>")
	text = text.replace("&lt;s&gt;", "<s>")
	text = text.replace("&lt;/s&gt;", "</s>")
	text = text.replace("&lt;u&gt;", "<u>")
	text = text.replace("&lt;/u&gt;", "</u>")
	text = text.replace("&lt;/a&gt;", "</a>")
	text = text.replace("&lt;/emoji&gt;", "</emoji>")
	link_search = re.findall(r"&lt;a href='\S+'&gt;", text)
	emoji_search = re.findall(r"&lt;emoji document_id=\d+&gt;", text)
	for i in link_search:
		t = i.replace("&lt;a", "<a")
		t = t.replace("&gt;", ">")
		text = text.replace(i, t)
	for e in emoji_search:
		t = e.replace("&lt;emoji", "<emoji")
		t = t.replace("&gt;", ">")
		text = text.replace(e, t)

	return text