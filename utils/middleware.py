import asyncio
import logging

import pyrogram
import pyrogram_patch
from pyrogram import types
from pyrogram_patch.middlewares.middleware_types import OnUpdateMiddleware
from pyrogram_patch.middlewares import PatchHelper

import utils


class RegUser(OnUpdateMiddleware):
	def __init__(self, *args, **kwargs):
		pass

	async def __call__(self, update: types.Update, client: pyrogram.Client, patch_helper: PatchHelper):
		if not isinstance(update, types.Message):
			return

		uid = update.from_user.id
		aus = utils.db.getAllUsers()
		user = utils.db.getUser(uid, True)
		if not user:
			user = utils.db.regUser(uid, True)
			if uid == utils.config['dev_id']:
				utils.db.save(f"UPDATE users SET status = 5 WHERE id = {utils.config['dev_id']}")

			out = f"🎧 <b><a href='tg://user?id={uid}'>Пользователь</a> (<a href='tg://openmessage?user_id=" \
				  f"{uid}'>*тык*</a>) создал новый аккаунт!</b>\n" \
				  f"🆔 <b>ID:<b> <code>{uid}</code>\n\n" \
				  f"<b><i>Всего аккаунтов: {len(aus)+1}</i></b>"
			cid = utils.config['admin_chat'] if utils.config['admin_chat'] != 0 else utils.config['dev_id']
			await utils.answer(
				update, out, False, cid
			)
		
		if user['status'] < 0:
			self.skip_handler()

		return

		# get_data() - use this method to get the data you saved earlier
		# skip_handler() - use this method to skip the handler
		# patch_helper.state.state - this way you can get the current state