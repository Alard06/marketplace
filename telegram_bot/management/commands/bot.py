import os

from django.core.management import BaseCommand

from marketplace.settings import API_KEY
from telegram_bot.models import *
from CustomUser.models import CustomUser

import telebot
from telebot import types

bot = telebot.TeleBot(API_KEY)


class Command(BaseCommand):
    help = 'Telegram bot '

    def handle(self, *args, **options):
        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            bot.send_message(message.from_user.id, 'Здравствуйте! Это бот администраторов маркетплейса "Барахолка"')
            bot.send_message(message.from_user.id, f'Чтобы получить доступ к админ-панели, напишите @alard666 и '
                                                   f'сообщите владельцу Ваш telegram id: {message.from_user.id}')

        @bot.message_handler(content_types=['text'])
        def send_message(message):
            print(message.text)
            print(message.from_user.id, Owner.objects.filter(telegram_id=message.chat.id).exists())
            if Owner.objects.filter(telegram_id=message.chat.id).exists():
                print(Owner.objects.get(telegram_id=message.from_user.id).role)
                if Owner.objects.filter(telegram_id=message.from_user.id, role='A').exists():
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    btn1 = types.KeyboardButton('Заявки')
                    markup.add(btn1)
                    bot.send_message(message.from_user.id, 'Выбери соответствующее действиеВ', reply_markup=markup)

                    if message.text == 'Заявки':
                        bot.send_message(message.from_user.id, f'Количество необработанных заявок составляет: {CustomUser.objects.filter().count()}')

                elif Owner.objects.filter(telegram_id=message.from_user.id, role='O').exists():
                    bot.send_message(message.from_user.id, 'Owner?')
                else:
                    bot.send_message(message.from_user.id, 'Ты кто?')
            else:
                bot.send_message(message.from_user.id, 'Врешь')

        bot.polling(none_stop=True, interval=0)
