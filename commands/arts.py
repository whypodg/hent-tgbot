import asyncio
import datetime
import hmtai
import html
import logging
import random
import requests

import pyrogram
import pyrogram_patch
from pyrogram import filters, types
from pyrogram_patch.router import Router

import utils
from utils import keyboards as kbs


arts = Router()
arts.name = "arts"


async def getScrolller(query: str):
	ans = requests.get(
		"https://api.scrolller.com/api/v2/graphql",
		json={
			"query": " query SubredditQuery( $url: String! $filter: SubredditPostFilter" \
					 " $iterator: String ) { getSubreddit(url: $url) { children(" \
					 " limit: 1 iterator: $iterator filter: $filter" \
					 " disabledHosts: null ) { iterator items {url subredditTitle" \
					 " isNsfw mediaSources { url } } } } } ",
			"variables": {"url": query, "filter": None, "hostsDown": None},
			"authorization": None
		}
	).json()

	posts = ans['data']['getSubreddit']['children']['items']
	return [post['mediaSources'][-1]['url'] for post in posts]



@arts.on_message(
	filters.command(commands=["hentai", "хентай"], prefixes=["/", "!"])
)
async def hentai(client: pyrogram.Client, message: types.Message):
	m = await utils.answer(message, "🕓 <i>Подождите…</i>")
	r = requests.get("https://api.waifu.im/search/?included_tags=hentai").json()

	await m.delete()
	await utils.answer_photo(
		message, r['images'][0]['url'],
		"<i>ммм 🤤</i>", reply_markup=kbs.kb_hent,
		has_spoiler=True
	)

@arts.on_callback_query(filters.regex("hentai"))
async def hentaiCB(client: pyrogram.Client, query: types.CallbackQuery):
	r = requests.get("https://api.waifu.im/search/?included_tags=hentai").json()
	await utils.edit_media(
		query.message,
		types.InputMediaPhoto(
			media=r['images'][0]['url'], has_spoiler=True,
			caption=utils.parseText(html.escape("<i>ммм 🤤</i>"))
		),
		reply_markup=kbs.kb_hent
	)


@arts.on_message(
	filters.command(commands=["milf", "милф"], prefixes=["/", "!"])
)
async def milf(client: pyrogram.Client, message: types.Message):
	m = await utils.answer(message, "🕓 <i>Подождите…</i>")
	r = requests.get("https://api.waifu.im/search/?included_tags=milf").json()

	await m.delete()
	await utils.answer_photo(
		message, r['images'][0]['url'],
		"<i>мне до неё ещё долго расти 😩</i>", reply_markup=kbs.kb_milf,
		has_spoiler=True
	)

@arts.on_callback_query(filters.regex("milf"))
async def milfCB(client: pyrogram.Client, query: types.CallbackQuery):
	r = requests.get("https://api.waifu.im/search/?included_tags=milf").json()
	await utils.edit_media(
		query.message,
		types.InputMediaPhoto(
			media=r['images'][0]['url'], has_spoiler=True,
			caption=utils.parseText(html.escape("<i>мне до неё ещё долго расти 😩</i>"))
		),
		reply_markup=kbs.kb_milf
	)


@arts.on_message(
	filters.command(commands=["ecchi", "ero", "этти", "эро"], prefixes=["/", "!"])
)
async def ecchi(client: pyrogram.Client, message: types.Message):
	m = await utils.answer(message, "🕓 <i>Подождите…</i>")
	r = requests.get("https://api.waifu.im/search/?included_tags=ecchi").json()

	await m.delete()
	await utils.answer_photo(
		message, r['images'][0]['url'],
		"<i>всякие пошлости специально для тебя 😏</i>", reply_markup=kbs.kb_ecchi,
		has_spoiler=True
	)

@arts.on_callback_query(filters.regex("ecchi"))
async def ecchiCB(client: pyrogram.Client, query: types.CallbackQuery):
	r = requests.get("https://api.waifu.im/search/?included_tags=ecchi").json()
	await utils.edit_media(
		query.message,
		types.InputMediaPhoto(
			media=r['images'][0]['url'], has_spoiler=True,
			caption=utils.parseText(html.escape("<i>всякие пошлости специально для тебя 😏</i>"))
		),
		reply_markup=kbs.kb_ecchi
	)



@arts.on_message(
	filters.command(commands=["futa", "trap", "фута", "трап"], prefixes=["/", "!"])
)
async def trap(client: pyrogram.Client, message: types.Message):
	m = await utils.answer(message, "🕓 <i>Подождите…</i>")
	r = requests.get("https://api.waifu.pics/nsfw/trap").json()

	await m.delete()
	await utils.answer_photo(
		message, r['url'],
		"<i>они большие 😳</i>", reply_markup=kbs.kb_trap,
		has_spoiler=True
	)

@arts.on_callback_query(filters.regex("trap"))
async def trapCB(client: pyrogram.Client, query: types.CallbackQuery):
	r = requests.get("https://api.waifu.pics/nsfw/trap").json()
	await utils.edit_media(
		query.message,
		types.InputMediaPhoto(
			media=r['url'], has_spoiler=True,
			caption=utils.parseText(html.escape("<i>они большие 😳</i>"))
		),
		reply_markup=kbs.kb_trap
	)


@arts.on_message(
	filters.command(commands=["neko", "неко"], prefixes=["/", "!"])
)
async def neko(client: pyrogram.Client, message: types.Message):
	m = await utils.answer(message, "🕓 <i>Подождите…</i>")
	r = requests.get("https://api.waifu.pics/nsfw/neko").json()

	await m.delete()
	await utils.answer_photo(
		message, r['url'],
		"<i>котики 😊</i>", reply_markup=kbs.kb_neko,
		has_spoiler=True
	)

@arts.on_callback_query(filters.regex("neko"))
async def nekoCB(client: pyrogram.Client, query: types.CallbackQuery):
	r = requests.get("https://api.waifu.pics/nsfw/neko").json()
	await utils.edit_media(
		query.message,
		types.InputMediaPhoto(
			media=r['url'], has_spoiler=True,
			caption=utils.parseText(html.escape("<i>котики 😊</i>"))
		),
		reply_markup=kbs.kb_neko
	)



@arts.on_message(
	filters.command(commands=["tentacles", "тентакли"], prefixes=["/", "!"])
)
async def tentacles(client: pyrogram.Client, message: types.Message):
	m = await utils.answer(message, "🕓 <i>Подождите…</i>")

	await m.delete()
	await utils.answer_photo(
		message, hmtai.get('hmtai', 'tentacles'),
		"<i>они лезут отовсюду 😖</i>", reply_markup=kbs.kb_tent,
		has_spoiler=True
	)

@arts.on_callback_query(filters.regex("tent"))
async def tentaclesCB(client: pyrogram.Client, query: types.CallbackQuery):
	await utils.edit_media(
		query.message,
		types.InputMediaPhoto(
			media=hmtai.get('hmtai', 'tentacles'), has_spoiler=True,
			caption=utils.parseText(html.escape("<i>они лезут отовсюду 😖</i>"))
		),
		reply_markup=kbs.kb_tent
	)


@arts.on_message(
	filters.command(commands=["foot", "фут"], prefixes=["/", "!"])
)
async def footJob(client: pyrogram.Client, message: types.Message):
	m = await utils.answer(message, "🕓 <i>Подождите…</i>")

	await m.delete()
	await utils.answer_photo(
		message, hmtai.get('hmtai', 'footjob'),
		"<i>ножки 😍</i>", reply_markup=kbs.kb_foot,
		has_spoiler=True
	)

@arts.on_callback_query(filters.regex("foot"))
async def footJobCB(client: pyrogram.Client, query: types.CallbackQuery):
	await utils.edit_media(
		query.message,
		types.InputMediaPhoto(
			media=hmtai.get('hmtai', 'footjob'), has_spoiler=True,
			caption=utils.parseText(html.escape("<i>ножки 😍</i>"))
		),
		reply_markup=kbs.kb_foot
	)


@arts.on_message(
	filters.command(commands=["orgy", "оргия"], prefixes=["/", "!"])
)
async def orgy(client: pyrogram.Client, message: types.Message):
	m = await utils.answer(message, "🕓 <i>Подождите…</i>")

	await m.delete()
	await utils.answer_photo(
		message, hmtai.get('hmtai', 'orgy'),
		"<i>как много людей 🙀</i>", reply_markup=kbs.kb_orgy,
		has_spoiler=True
	)

@arts.on_callback_query(filters.regex("orgy"))
async def orgyCB(client: pyrogram.Client, query: types.CallbackQuery):
	await utils.edit_media(
		query.message,
		types.InputMediaPhoto(
			media=hmtai.get('hmtai', 'orgy'), has_spoiler=True,
			caption=utils.parseText(html.escape("<i>как много людей 🙀</i>"))
		),
		reply_markup=kbs.kb_orgy
	)


@arts.on_message(
	filters.command(commands=["bdsm", "бдсм"], prefixes=["/", "!"])
)
async def bdsm(client: pyrogram.Client, message: types.Message):
	m = await utils.answer(message, "🕓 <i>Подождите…</i>")

	await m.delete()
	await utils.answer_photo(
		message, hmtai.get('hmtai', 'bdsm'),
		"<i>АХ~.. ещё… 🥵</i>", reply_markup=kbs.kb_bdsm,
		has_spoiler=True
	)

@arts.on_callback_query(filters.regex("bdsm"))
async def bdsmCB(client: pyrogram.Client, query: types.CallbackQuery):
	await utils.edit_media(
		query.message,
		types.InputMediaPhoto(
			media=hmtai.get('hmtai', 'bdsm'), has_spoiler=True,
			caption=utils.parseText(html.escape("<i>АХ~.. ещё… 🥵</i>"))
		),
		reply_markup=kbs.kb_bdsm
	)


@arts.on_message(
	filters.command(commands=["wallpaper", "wall", "обои"], prefixes=["/", "!"])
)
async def wall(client: pyrogram.Client, message: types.Message):
	m = await utils.answer(message, "🕓 <i>Подождите…</i>")

	await m.delete()
	await utils.answer_photo(
		message, hmtai.get('hmtai', 'nsfwMobileWallpaper'),
		"<i>лови обои, семпай! 😏</i>", reply_markup=kbs.kb_wall,
		has_spoiler=True
	)

@arts.on_callback_query(filters.regex("wall"))
async def wallCB(client: pyrogram.Client, query: types.CallbackQuery):
	await utils.edit_media(
		query.message,
		types.InputMediaPhoto(
			media=hmtai.get('hmtai', 'nsfwMobileWallpaper'), has_spoiler=True,
			caption=utils.parseText(html.escape("<i>лови обои, семпай! 😏</i>"))
		),
		reply_markup=kbs.kb_wall
	)


@arts.on_message(
	filters.command(commands=["ahegao", "ахегао"], prefixes=["/", "!"])
)
async def face(client: pyrogram.Client, message: types.Message):
	m = await utils.answer(message, "🕓 <i>Подождите…</i>")

	await m.delete()
	await utils.answer_photo(
		message, hmtai.get('hmtai', 'ahegao'),
		"<i>это личико… 🤤</i>", reply_markup=kbs.kb_face,
		has_spoiler=True
	)

@arts.on_callback_query(filters.regex("ahegao"))
async def faceCB(client: pyrogram.Client, query: types.CallbackQuery):
	await utils.edit_media(
		query.message,
		types.InputMediaPhoto(
			media=hmtai.get('hmtai', 'ahegao'), has_spoiler=True,
			caption=utils.parseText(html.escape("<i>это личико… 🤤</i>"))
		),
		reply_markup=kbs.kb_face
	)


@arts.on_message(
	filters.command(commands=["gif", "гиф"], prefixes=["/", "!"])
)
async def gif(client: pyrogram.Client, message: types.Message):
	m = await utils.answer(message, "🕓 <i>Подождите…</i>")

	await m.delete()
	await utils.answer_anim(
		message, hmtai.get('hmtai', 'gif'),
		"<i>лови гифку, семпай! 🎥😏</i>", reply_markup=kbs.kb_gif,
		has_spoiler=True
	)

@arts.on_callback_query(filters.regex("gif"))
async def gifCB(client: pyrogram.Client, query: types.CallbackQuery):
	await utils.edit_media(
		query.message,
		types.InputMediaAnimation(
			media=hmtai.get('hmtai', 'gif'), has_spoiler=True,
			caption=utils.parseText(html.escape("<i>лови гифку, семпай! 🎥😏</i>"))
		),
		reply_markup=kbs.kb_gif
	)



@arts.on_message(
	filters.command(commands=["furry", "yiff", "фурри"], prefixes=["/", "!"])
)
async def yiff(client: pyrogram.Client, message: types.Message):
	m = await utils.answer(message, "🕓 <i>Подождите…</i>")
	links = await getScrolller("yiff")

	await m.delete()
	await utils.answer_photo(
		message, random.choice(links),
		"<i>люблю зверушек 😗</i>", reply_markup=kbs.kb_yiff,
		has_spoiler=True
	)

@arts.on_callback_query(filters.regex("yiff"))
async def yiffCB(client: pyrogram.Client, query: types.CallbackQuery):
	links = await getScrolller("yiff")

	await utils.edit_media(
		query.message,
		types.InputMediaPhoto(
			media=random.choice(links), has_spoiler=True,
			caption=utils.parseText(html.escape("<i>люблю зверушек 😗</i>"))
		),
		reply_markup=kbs.kb_yiff
	)


@arts.on_message(
	filters.command(commands=["yuri", "юри"], prefixes=["/", "!"])
)
async def yuri(client: pyrogram.Client, message: types.Message):
	m = await utils.answer(message, "🕓 <i>Подождите…</i>")
	links = await getScrolller(
		random.choice(['yuri', 'yurihentai'])
	)

	await m.delete()
	await utils.answer_photo(
		message, random.choice(links),
		"<i>милашки ❤</i>", reply_markup=kbs.kb_yuri,
		has_spoiler=True
	)

@arts.on_callback_query(filters.regex("yuri"))
async def yuriCB(client: pyrogram.Client, query: types.CallbackQuery):
	links = await getScrolller(
		random.choice(['yuri', 'yurihentai'])
	)

	await utils.edit_media(
		query.message,
		types.InputMediaPhoto(
			media=random.choice(links), has_spoiler=True,
			caption=utils.parseText(html.escape("<i>милашки ❤</i>"))
		),
		reply_markup=kbs.kb_yuri
	)


@arts.on_message(
	filters.command(commands=["yaoi", "яой"], prefixes=["/", "!"])
)
async def yaoi(client: pyrogram.Client, message: types.Message):
	m = await utils.answer(message, "🕓 <i>Подождите…</i>")
	links = await getScrolller(
		random.choice(["yaoi", "yaoinsfw"])
	)

	await m.delete()
	await utils.answer_photo(
		message, random.choice(links),
		"<i>мальчики просто развлекаются 😏</i>", reply_markup=kbs.kb_yaoi,
		has_spoiler=True
	)

@arts.on_callback_query(filters.regex("yaoi"))
async def yaoiCB(client: pyrogram.Client, query: types.CallbackQuery):
	links = await getScrolller(
		random.choice(["yaoi", "yaoinsfw"])
	)

	await utils.edit_media(
		query.message,
		types.InputMediaPhoto(
			media=random.choice(links), has_spoiler=True,
			caption=utils.parseText(html.escape("<i>мальчики просто развлекаются 😏</i>"))
		),
		reply_markup=kbs.kb_yaoi
	)