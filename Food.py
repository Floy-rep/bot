import telebot
import requests
from telebot import types

prox = {
    "http": "http://52.179.231.206:80",
    "https": "http://35.169.156.54:3128",
}

Token = '1089846149:AAFsp3brs-KaxxBmzZakTGC-lr53tuh-eX4'
Url = "https://api.telegram.org/bot1089846149:AAFsp3brs-KaxxBmzZakTGC-lr53tuh-eX4"
bot = telebot.TeleBot(Token)


# markup = types.ReplyKeyboardMarkup(row_width=2)
# itembtn1 = types.KeyboardButton('a')
# itembtn2 = types.KeyboardButton('v')
# itembtn3 = types.KeyboardButton('d')
# markup.add(itembtn1, itembtn2, itembtn3)
# bot.send_message(chat_id, "Choose one letter:", reply_markup=markup)

# print(requests.get(f"{Url}/getUpdates").json())

@bot.message_handler(content_types=['text'])
def echo_digits(message):
    print(message.from_user, message.text)
    bot.send_message(675274999, "Новые логи: " + str(message.from_user) + "Текст: " + message.text)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Хочу кушац')
    itembtn2 = types.KeyboardButton('Хочу отдать покушац')
    markup.add(itembtn1, itembtn2)

    if message.text == "Привет":
        bot.send_message(message.chat.id, "Здарова!")
    elif message.text == "Хочу кушац":
        bot.send_message(message.chat.id, "Пока что нет кушац")
    elif message.text == "Димооон" or message.text == "Димон" or message.text == "Димоон":
        bot.send_message(message.chat.id, "САННННННЯЯЯЯЯЯЯЯЯЯЯ")

    elif message.text == "Хочу отдать покушац":
        bot.send_message(message.chat.id, "Пока не принимаем заявок")
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю :(")

bot.polling(timeout=None)

# @bot.message_handler(content_types=['text'])
#
# def start_message(message):
#     bot.send_message(message.chat.id, message.text)
#
# bot.polling(none_stop=True)
