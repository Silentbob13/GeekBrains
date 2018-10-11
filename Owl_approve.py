import random
import telebot
import requests
import imghdr
from PIL import Image
from telebot.types import Message


answer_list=["Подтверждаю","Не уверен", "Так точно", "Не в этот раз"]
TOKEN = ''

bot= telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start_help(message):
    bot.send_message(message.chat.id,"""Вас приветствует Подтверждающий Филин, Вы можете отправлять ему любые сообщения
Но для начала вводная:

Царь позвал к себе Иванушку-дурака и говорит:
-Если завтра не принесешь двух говорящих птиц голову срублю.
Иван принес филина и воробья.
Царь говорит: -Ну, пусть что-нибудь скажут.
Иван спрашивает: -Воробей,почем раньше водка в магазине была?
Воробей: -Чирик.
Иван филину: -А ты,филин,подтверди.
Филин: -Подтверждаю!""")

@bot.message_handler(content_types=['sticker'])
def reply_to_sticker(message: Message):
    file_info=bot.get_file(message.sticker.file_id)
    res=bot.download_file(file_info.file_path)
    bot.send_message(message.chat.id,message.sticker.emoji)
    bot.send_photo(message.chat.id,res)
    
@bot.message_handler(func=lambda message: True)
def reply_to_user_message(message: Message):
    if (message.text.find('подтверди')>-1 or message.text.find('Подтверди')>-1): 
        bot.send_message(message.chat.id,random.choice(answer_list))
    else:
        if(random.randint(0, 10)>6):
            bot.send_message(message.chat.id,"Угу")

bot.polling()
