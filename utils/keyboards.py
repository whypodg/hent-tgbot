import pyrogram
from pyrogram import types
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


kb_ping = [
	[InlineKeyboardButton(text="Повторить", callback_data="ping")]
]
kb_ping = InlineKeyboardMarkup(kb_ping)


kb_help = [
	[InlineKeyboardButton(text="📝 Список команд", url="https://teletype.in/@whypodg/hent-cmd")],
	[InlineKeyboardButton(text="➕ Добавить в чат", url="https://t.me/henttgbot?startgroup=start")],
	[InlineKeyboardButton(text="💬 Наш чат", url="https://t.me/henttgchat")]
]
kb_help = InlineKeyboardMarkup(kb_help)


kb_hent = [[InlineKeyboardButton(text="Ещё хентай 🤤", callback_data="hentai")]]
kb_hent = InlineKeyboardMarkup(inline_keyboard=kb_hent)

kb_milf = [[InlineKeyboardButton(text="Ещё милфы 😮‍💨", callback_data="milf")]]
kb_milf = InlineKeyboardMarkup(inline_keyboard=kb_milf)

kb_ecchi = [[InlineKeyboardButton(text="Ещё этти 😏", callback_data="ecchi")]]
kb_ecchi = InlineKeyboardMarkup(inline_keyboard=kb_ecchi)

kb_tent = [[InlineKeyboardButton(text="Ещё тентакли 😳", callback_data="tent")]]
kb_tent = InlineKeyboardMarkup(inline_keyboard=kb_tent)

kb_foot = [[InlineKeyboardButton(text="Ещё ножки 🦶", callback_data="foot")]]
kb_foot = InlineKeyboardMarkup(inline_keyboard=kb_foot)

kb_orgy = [[InlineKeyboardButton(text="Ещё оргия 🥵", callback_data="orgy")]]
kb_orgy = InlineKeyboardMarkup(inline_keyboard=kb_orgy)

kb_wall = [[InlineKeyboardButton(text="Ещё обои 🖼", callback_data="wall")]]
kb_wall= InlineKeyboardMarkup(inline_keyboard=kb_wall)

kb_yuri = [[InlineKeyboardButton(text="Ещё юри ❤", callback_data="yuri")]]
kb_yuri = InlineKeyboardMarkup(inline_keyboard=kb_yuri)

kb_yaoi = [[InlineKeyboardButton(text="Ещё яой 😏", callback_data="yaoi")]]
kb_yaoi = InlineKeyboardMarkup(inline_keyboard=kb_yaoi)

kb_yiff = [[InlineKeyboardButton(text="Ещё фурри 😸", callback_data="yiff")]]
kb_yiff = InlineKeyboardMarkup(inline_keyboard=kb_yiff)

kb_face = [[InlineKeyboardButton(text="Ещё ахегао 🤤", callback_data="ahegao")]]
kb_face = InlineKeyboardMarkup(inline_keyboard=kb_face)

kb_gif = [[InlineKeyboardButton(text="Ещё гифки 🎦", callback_data="gif")]]
kb_gif = InlineKeyboardMarkup(inline_keyboard=kb_gif)

kb_bdsm = [[InlineKeyboardButton(text="Ещё бдсм 🥵", callback_data="bdsm")]]
kb_bdsm = InlineKeyboardMarkup(inline_keyboard=kb_bdsm)

kb_trap = [[InlineKeyboardButton(text="Ещё трапы 😳", callback_data="trap")]]
kb_trap = InlineKeyboardMarkup(inline_keyboard=kb_trap)

kb_neko = [[InlineKeyboardButton(text="Ещё неко 😊", callback_data="neko")]]
kb_neko = InlineKeyboardMarkup(inline_keyboard=kb_neko)