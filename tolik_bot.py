import asyncio
from pyrogram import Client, filters
from random import choice, random, randrange
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
    'Я полностью "за"'
]

@app.on_message()
async def react_to_video_message(_, message):
    print(message)
    # Tolik
    is_tolik = message.from_user.id == 596655936
    #
    if is_tolik and bool(random.getrandbits(1)):
        await asyncio.sleep(randrange(5))
        reaction = choice(reactions)
        message.reply(reaction)

task = asyncio.create_task(app.run())
event_loop = asyncio.get_event_loop()
event_loop.run_until_complete()