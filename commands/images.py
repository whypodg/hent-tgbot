import asyncio
import datetime
import logging
import requests

import pyrogram
import pyrogram_patch
from pyrogram import filters, types
from pyrogram_patch.router import Router

import utils
from utils import keyboards as kbs


images = Router()
images.name = "images"


@images.on_message(
	filters.command(commands=["checknsfw", "чекнсфв"], prefixes=["/", "!"])
)
async def checkNsfw(client: pyrogram.Client, message: types.Message):
	if not utils.config['wtoken']:
		await utils.answer(
			message,
			f"☹ <b>API для проверки фотографий на наличие NSFW недоступно, причина этому — отсутствие токена для доступа к API.</b>\n" \
			f"Свяжитесь с <a href='tg://user?id={utils.config['dev_id']}'></a>"
		)
		return

	msg = message.reply_to_message or message
	if not msg.photo:
		await utils.answer(
			message,
			"❗ <b>Прикрепите фото, или ответьте на него</b>, иначе я не пойму, что проверять"
		)
		return

	photo = msg.photo.file_id
	media = (await client.download_media(
		message=photo, in_memory=True
	)).getbuffer()

	r = requests.post(
		"https://nsfw.whypodg.me/check",
		params={
			"access_token": utils.config['wtoken']
		},
		files=[("file", ("file.png", media))]
	).json()['data']

	await utils.answer(
		message,
		f"🖼 <b>Информация об изображении:</b>\n\n" \
		f"🔞 <b>NSFW:</b> {'✅' if r['is_nsfw'] else '❌'}\n" \
		f"📂 <b>Классификации:</b>\n" \
		f"  • 🖌 <b>Арт (безопасно):</b> <code>{round(r['drawings'], 2)}%</code>\n" \
		f"  • 🛡 <b>Нейтральное фото (безопасно):</b> <code>{round(r['neutral'], 2)}%</code>\n" \
		f"  • 🍑 <b>Эротика (безопасно(?)):</b> <code>{round(r['sexy'], 2)}%</code>\n" \
		f"  • 🌚 <b>Хентай (NSFW):</b> <code>{round(r['hentai'], 2)}%</code>\n" \
		f"  • 🔞 <b>Порно (NSFW):</b> <code>{round(r['porn'], 2)}%</code>"
	)