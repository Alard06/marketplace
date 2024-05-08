import os

from django.core.management import BaseCommand

from marketplace.settings import API_KEY
from telegram_bot.models import *
from apps.seller.models import SellerApplication

import telebot
from telebot import types


class Command(BaseCommand):
    help = 'Telegram bot '

    def handle(self, *args, **options):
        bot = telebot.TeleBot(API_KEY)

        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            bot.send_message(message.from_user.id, 'Здравствуйте! Это бот администраторов маркетплейса "Барахолка"')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('/enter')
            markup.add(btn1)
            bot.send_message(message.from_user.id, f'Чтобы получить доступ к админ-панели, напишите @alard666 и '
                                                   f'сообщите владельцу Ваш telegram id: {message.from_user.id}\n'
                                                   f'После получения доступа, можете нажать на кнопку "/enter"', reply_markup=markup)

        @bot.message_handler(commands=['enter'])
        def enter_user(message):
            print(message.from_user.id)
            user = True if Owner.objects.filter(telegram_id=message.chat.id).exists() else False
            role = Owner.objects.get(telegram_id=message.chat.id).role
            print(role)
            if role in 'AO':
                print('AO')
                markup = types.ReplyKeyboardMarkup()
                if role == 'O':
                    btn1 = types.KeyboardButton('/add_administrator')
                    btn2 = types.KeyboardButton('/orders')
                    btn3 = types.KeyboardButton('/work')
                    markup.add(btn1, btn2, btn3)
                else:
                    btn2 = types.KeyboardButton('/orders')
                    btn3 = types.KeyboardButton('/work')
                    markup.add(btn2, btn3)
                bot.send_message(message.from_user.id, f'Выберите операцию: ', reply_markup=markup)

        @bot.message_handler(commands=['orders'])
        def send_message(message):
            role = Owner.objects.get(telegram_id=message.chat.id).role
            if role in 'AO':
                bot.send_message(message.from_user.id, f'Количество необработанных заявок: {SellerApplication.objects.all().count()}', reply_markup='')
        def show_applications(message):
            applications = SellerApplication.objects.all().count()
            bot.send_message(message.from_user.id, f'Количество заявок: {applications}')

        bot.polling(none_stop=True, interval=0)     q
