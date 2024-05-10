import os

from django.core.management import BaseCommand

from CustomUser.models import CustomUser
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
                                                   f'После получения доступа, можете нажать на кнопку "/enter"',
                             reply_markup=markup)

        @bot.message_handler(commands=['enter'])
        def enter_user(message):
            print(message.from_user.id)
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
            if check_role(message):
                bot.send_message(message.from_user.id,
                                 f'Количество необработанных заявок: {SellerApplication.objects.all().count()}')

        @bot.message_handler(commands=['work'])
        def send_work(message):
            if check_role(message):
                markup = types.ReplyKeyboardMarkup()
                msg, first_application = format_message(message)
                if not first_application == '...':
                    btn1 = types.KeyboardButton('Одобрить')
                    btn2 = types.KeyboardButton('Отклонить')
                    markup.add(btn1, btn2)
                    bot.send_message(message.from_user.id, msg, reply_markup=markup)
                    bot.register_next_step_handler(message, work_application)
                else:
                    btn1 = types.KeyboardButton('/enter')
                    markup.add(btn1)
                    bot.send_message(message.from_user.id, 'Ждем заявки', reply_markup=markup)

        def work_application(message):
            if message.text.lower() == 'одобрить':
                application = SellerApplication.objects.first()
                CustomUser.objects.create(
                    first_name=application.first_name,
                    last_name=application.last_name,
                    email=application.email,
                    telephone_number=application.phone_number,
                    inn=application.inn,
                    permission_to_sell=True,
                    seller=True,
                    username=application.name
                )
                SellerApplication.objects.first().delete()
                bot.send_message(message.from_user.id, 'Заявка одобрена..')

        def check_role(message):
            role = Owner.objects.get(telegram_id=message.chat.id).role
            if role in 'AO':
                return True
            else:
                return False

        def format_message(message):
            first_application = SellerApplication.objects.first()
            if first_application:
                msg = (f'Фамилия: {first_application.last_name}\n'
                       f'Имя: {first_application.first_name}\n'
                       f'Отчество: {first_application.patronymic}\n'
                       f'INN: {first_application.inn}\n'
                       f'Название магазина: {first_application.name}\n'
                       f'Email: {first_application.email}\n'
                       f'Номер телефона: {first_application.phone_number}\n'
                       f'Доп. информация: {first_application.description}')
                return msg, first_application
            else:
                return 'Заявок нету', '...'

        bot.polling(none_stop=True, interval=0)
