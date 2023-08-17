# Hentai Bot для Telegram (RU)
Это — исходный код проекта [🌚 Hentai Bot](https://henttgbot.t.me)

## Настройка конфига
Вот дефолтное значение конфига:
```json
{
    "token": "",
    "id": 0,
    "dev_id": 0,
    "admin_chat": 0,
    "version": "2.0.0",
    "wtoken": "",
    "app": {
        "id": 0,
        "hash": ""
    },
    "commands": {
        "admin": true,
        "arts": true,
        "images": true,
        "other": true
    }
}
```
Вот описание значений:
| Значение | Описание |
|:---------:|:---------:|
| token | Токен бота, который можно взять в [@BotFather](https://BotFather.t.me) |
| id | ID бота |
| dev_id | Ваш ID |
| admin_chat | ID админ-чата, куда будут присылаться логи |
| version | Версия бота |
| wtoken | Token для доступа к API для проверки изображений на NSFW **(можно не указывать)** |
| app -> id | API ID вашего приложения, подробнее — [Создание приложения](https://github.com/whypodg/hent-tgbot#Создание-приложения) |
| app -> hash | API HASH вашего приложения, подробнее — [Создание приложения](https://github.com/whypodg/hent-tgbot#Создание-приложения) |
| commands | Значения в этом словаре отвечают за работу роутеров. `true` — включен, `false` — выключен |

## Создания приложения
Заходим на [my.telegram.org](https://my.telegram.org), авторизуемся и нажимаем на `API development tools`
<img src="https://github.com/whypodg/hent-tgbot/raw/main/data/my_tg_org.png"></img>
### Если у вас нет приложения, страница будет выглядеть так:
<img src="https://github.com/whypodg/hent-tgbot/raw/main/data/api_tools_noapp.png"></img>
В таком случае вводим в `App title` и `Short name` любые значения, **остальное не трогаем**
### Если же у вас есть приложение, страница будет выглядеть так:
<img src="https://github.com/whypodg/hent-tgbot/raw/main/data/api_tools_app.png"></img>
В таком случае берем `App api_id` и `App api_hash` и вставляем в конфиг