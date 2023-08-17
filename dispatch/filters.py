import typing

import pyrogram
from pyrogram import filters, types, enums

import utils


def status_filter(status: int):
	async def func(flt, _, update: types.Update):
		if isinstance(update, types.Message):
			uid = update.from_user.id or update.from_user.id
			msg = update
		elif isinstance(update, CallbackQuery):
			uid = update.from_user.id
			msg = update.message

		us = utils.getUser(uid)
		if not us or us[0][1] < status:
			prem = f"⚠ <b>Эту команду могут использовать только 👑 <u>Premium-пользователи</u>!</b>"
			stat = f"🏮 <b>Ой, что?</b>\nНазови мне хотя бы одну весомую причину, почему я должен делать это для <b>тебя</b>"
			out = stat if status != 1 else prem
			await utils.answer(
				msg, out
			)
			return False
		return True if us[0][1] >= status else False

	return filters.create(
		func, status=status
	)