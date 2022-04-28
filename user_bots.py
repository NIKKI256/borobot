from pyrogram import Client, filters
from decouple import config
from consts import compliments, agree_reactions
from random import choice, randrange
from time import sleep

APP_ID = config('APP_ID')
APP_HASH = config('APP_HASH')

LOVE_ID = config('LOVE_ID', cast=int)
TOLIK_ID = config('TOLIK_ID', cast=int)

app = Client('my_account', api_id=APP_ID, api_hash=APP_HASH)

# @app.on_message()
# def check_info_about_message(_, message):
    # 1. Uncomment prints below
    # print(f'Hello here you can find out id of person {message.from_user.id}')
    # print(f'Here is name of person {message.from_user.first_name}')
    # print(f'Here is username of person {message.from_user.username}')
    # 2. After it you can comment lines above
    # pass

@app.on_message(filters.user(users=LOVE_ID))
def react_to_video_message_of_love(_, message):
    """
    react_to_video_message_of_love: 
    this function react to video messages of your love

    message: dict you get from users in telegram
    """
    #
    is_video_message = getattr(message, 'video_note', False)
    #
    if is_video_message:
        compliment_message = choice(compliments)
        message.reply(compliment_message)


@app.on_message(filters.user(users=TOLIK_ID))
def react_to_message(_, message):
    """
    react_to_video_message_of_love: 
    this function randomly react to messages of analytics 

    message: dict you get from users in telegram
    """
    #
    is_react_to_message = bool(randrange(5) == 3)
    #
    if is_react_to_message:
        sleep(randrange(3,5))
        reaction = choice(agree_reactions)
        message.reply(reaction)

app.run()