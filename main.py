import requests
import telebot
from telebot import types

bot = telebot.TeleBot('1422338941:AAH0_2aUp_Th6AX0pVGRMP1vY48fpIPApLk')

keyboard = types.InlineKeyboardMarkup()

key_news_polit = types.InlineKeyboardButton(text='Новости жопы', callback_data='polit')
keyboard.add(key_news_polit)

key_open_youtube = types.InlineKeyboardButton(text='Мне нечего делать', callback_data='youtube')
keyboard.add(key_open_youtube)

key_news_it = types.InlineKeyboardButton(text='Твою ж, у меня сегодня кванториум! Покажи их новости', callback_data='it')
keyboard.add(key_news_it)

key_news_covid = types.InlineKeyboardButton(text='Коронавирус-корона, уходи с нашего района', callback_data='covid')
keyboard.add(key_news_covid)

key_weather = types.InlineKeyboardButton(text='Лень смотреть в окно, чё там за апокалипсис происходит?', callback_data='weather')
keyboard.add(key_weather)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'youtube':
        bot.send_message(call.message.chat.id, "https://www.youtube.com/")
    elif call.data == 'weather':
        weather = requests.get('https://yandex.ru/pogoda/sarov?utm_source=serp&utm_campaign=wizard&utm_medium=desktop&utm_content=wizard_desktop_main&utm_term=title')
        bot.send_message(call.message.chat.id, weather)
    else:
        bot.send_message(call.message.chat.id, "Спустись с небес на землю, идиот")

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Пошёл в жопу, ИЛИ куда Вам угодно, кожанный")
        bot.send_message(message.from_user.id,"Чё те надо? Я не нанимался на тебя работать!", reply_markup=keyboard)
    elif message.text == "привет":
        bot.send_message(message.from_user.id, "С заглавной буквы пиши, кожанный")
        bot.send_message(message.from_user.id, "Чё те надо? Я не нанимался на тебя работать!", reply_markup=keyboard)
    elif message.text == "ghbdtn":
        bot.send_message(message.from_user.id, "Куда ты меня послал?")
        bot.send_message(message.from_user.id, "Научась писать /help, для начала тебе, глупцу, сойдёт")
    elif message.text == "Здравствуйте, господин Жопа, я поклоняюсь тебе, ОООООО мой Повелитель":
        bot.send_message(message.from_user.id, "Так бы сразу")
        bot.send_message(message.from_user.id, "Чё те надо? Я не нанимался на тебя работать!", reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши: Здравствуйте, господин Жопа, я поклоняюсь тебе, ОООООО мой Повелитель")
    else:
        bot.send_message(message.from_user.id, "Научась писать /help, для начала тебе, глупцу, сойдёт")


bot.polling(none_stop=True, interval=0)