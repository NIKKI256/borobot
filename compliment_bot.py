from pyrogram import Client
from random import choice
from decouple import config

APP_ID = config('APP_ID')
APP_HASH = config('APP_HASH')
LOVE_ID = config('LOVE_ID', cast=int)

app = Client('my_account', api_id=APP_ID, api_hash=APP_HASH)

compliments = [
    'Боже, какая же ты красивая',
    'Ты с каждым видео все лучше и лучше',
    'У меня сейчас будет передоз красоты в мозгах',
    'Именно ради такой и надо становиться богатым',
    'Вообще законно быть такой красивой?',
    'Я мог бы всю жизнь думать о тебе и мне бы не надоело'
]

@app.on_message()
def react_to_video_message(_, message):
    # After it you can comment lines below 
    # print(f'Hello here you can find out id of your love {message.from_user.id}')
    # print(f'Here is name of person {message.from_user.first_name}')
    # print(f'Here is username of person {message.from_user.username}')
    #
    is_lovely_person = message.from_user.id == LOVE_ID
    is_video_message = getattr(message, 'video_note', False)
    #
    if is_lovely_person and is_video_message:
        compliment_message = choice(compliments)
        message.reply(compliment_message)

app.run()