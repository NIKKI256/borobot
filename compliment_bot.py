from pyrogram import Client, filters
from random import choice
from decouple import config

app = Client('my_account')

compliments = [
    'Боже, какая же ты красивая',
    'Ты с каждым видео все лучше и лучше',
    'У меня сейчас будет передоз красоты в мозгах',
    'Именно ради такой и надо становиться богатым'
]

@app.on_message()
def react_to_video_message(_, message):
    # After it you can comment lines below 
    # print(f'Hello here you can find out id of your love {message.from_user.id}')
    # print(f'Here is name of person {message.from_user.first_name}')
    # print(f'Here is username of person {message.from_user.username}')
    #
    # Replace 00000 to correct message.from_user.id
    is_lovely_person = message.from_user.id == 00000
    is_video_message = getattr(message, 'video_note')
    #
    if is_lovely_person and is_video_message:
        compliment_message = choice(compliments)
        message.reply(compliment_message)

app.run()