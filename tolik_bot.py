import asyncio
from pyrogram import Client
from random import choice, randrange, getrandbits
from decouple import config

APP_ID = config('APP_ID')
APP_HASH = config('APP_HASH')

app = Client('my_account', api_id=APP_ID, api_hash=APP_HASH)

reactions = [
    'Поддерживаю',
    'Полностью согласен',
    'Да, лучше и не скажешь',
    'Именно, как всегда прав',
    'С языка снял',
    'Лаконично',
    'Совершенно верно',
    'Аргументировано',
    'Несомненно',
    'Я того же мнения',
    'Это именно то, что я собирался сказать',
    'Я полностью "за"',
    'даже и не поспоришь!',
    'Братан УРААА!!!!'
]

@app.on_message()
async def react_to_message(_, message):
    is_tolik = message.from_user and message.from_user.id == 596655936
    #
    if is_tolik and bool(getrandbits(1)):
        await asyncio.sleep(randrange(3,5))
        reaction = choice(reactions)
        await message.reply(reaction)

asyncio.wait(app.run())