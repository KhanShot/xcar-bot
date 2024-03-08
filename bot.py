import os

import telebot
from telebot import types
bot = telebot.TeleBot("7130422920:AAF74IirT7yjHjSo7DHuQlM_INX097ezntM")



@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = "Добро пожаловать в систему xcar! 🚙 \n\nXcar - агрегатор, который формирует анкеты автовладельцев, которые быстро хотят продать свой автомобиль. \n\nДанный бот будет присылать горячие предложения. Не забудьте включить уведомления, чтобы не пропустить  выгодные предложения. \n\nУдачи!🔥"
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    key_yes = types.InlineKeyboardButton(text='🚀 Начать прием анкет', callback_data='start_get_forms')
    key_web = types.InlineKeyboardButton(text='🖥️ Наш сайт', callback_data='web_link', url="https://xcar.kz")
    key_msg = types.InlineKeyboardButton(text='💬 Связаться с менеджером', callback_data='send_message', url="https://t.me/bwzone")
    img = open("img.png", 'rb')
    keyboard.add(key_yes, key_web, key_msg)
    
    bot.send_photo(message.from_user.id, img ,caption=text, reply_markup=keyboard)
    


@bot.callback_query_handler(func=lambda call: True) 
def response_button(call):
    if (call.data == "start_get_forms"):
        bot.send_message(call.message.chat.id, 'Данный бот будет присылать горячие предложения автоматический после регистрации на сайте.')
        

bot.polling(none_stop=True, interval=0)
