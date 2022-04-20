from pyrogram import Client, filters
from decouple import config
from consts import compliments, agree_reactions
from random import choice, randrange, getrandbits
import asyncio

APP_ID = config('APP_ID')
APP_HASH = config('APP_HASH')

LOVE_ID = config('LOVE_ID', cast=int)
TOLIK_ID = config('TOLIK_ID', cast=int)

app = Client('my_account', api_id=APP_ID, api_hash=APP_HASH)


@app.on_message(filters.user(users=LOVE_ID))
async def react_to_video_message_of_love(_, message):
    # After it you can comment lines below 
    # print(f'Hello here you can find out id of your love {message.from_user.id}')
    # print(f'Here is name of person {message.from_user.first_name}')
    # print(f'Here is username of person {message.from_user.username}')
    #
    is_video_message = getattr(message, 'video_note', False)
    #
    if is_video_message:
        compliment_message = choice(compliments)
        await message.reply(compliment_message)


@app.on_message(filters.user(users=TOLIK_ID))
async def react_to_message(_, message):
    #
    is_react_to_message = bool(getrandbits(1))
    #
    if is_react_to_message:
        await asyncio.sleep(randrange(3,5))
        reaction = choice(agree_reactions)
        await message.reply(reaction)

app.run()