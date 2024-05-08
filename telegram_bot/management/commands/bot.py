from django.core.management.base import BaseCommand
from marketplace.settings import API_KEY

import telebot

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, 'Здравствуйте! Это бот администраторов маркетплейса "Барахолка"')
    bot.send_message(message.from_user.id, 'Чтобы получить доступ к админ-панели, напишите @alard666')

bot.polling(none_stop=True, interval=0)

@bot.message_handler(content_types=['text'])
def send_message(message):
    pass
