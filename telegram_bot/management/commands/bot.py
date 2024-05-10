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
            check, role = check_role(message)
            if check:
                markup = types.ReplyKeyboardMarkup()
                if role == 'O':
                    btn1 = types.KeyboardButton('/add_administrator')
                    btn2 = types.KeyboardButton('/orders')
                    btn3 = types.KeyboardButton('/work')
                    btn4 = types.KeyboardButton('/delete_administrator')
                    markup.add(btn1, btn4, btn2, btn3)
                else:
                    btn2 = types.KeyboardButton('/orders')
                    btn3 = types.KeyboardButton('/work')
                    markup.add(btn2, btn3)
                bot.send_message(message.from_user.id, f'Выберите операцию: ', reply_markup=markup)

        @bot.message_handler(commands=['orders'])
        def send_message(message):
            _, check = check_role(message)
            if check:
                bot.send_message(message.from_user.id,
                                 f'Количество необработанных заявок: {SellerApplication.objects.all().count()}')

        @bot.message_handler(commands=['work'])
        def send_work(message):
            _, check = check_role(message)
            if check:
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

        @bot.message_handler(commands=['add_administrator'])
        def add_administrator(message):
            check, role = check_role(message)
            if role == 'O':
                bot.send_message(message.from_user.id,
                                 'Введите через пробел данные об новом администраторе\ntelegram_id first_name last_name role(A,O)\n ВАЖНО: ПОЛЯ ПРОПУСКАТЬ НЕЛЬЗЯ!')
                bot.register_next_step_handler(message, add_admin)

        @bot.message_handler(commands=['delete_administrator'])
        def delete_administrator(message):
            check, role = check_role(message)
            if role == 'O':
                if Owner.objects.filter(role='A').count() != 0:
                    bot.send_message(message.from_user.id,
                                     format_administrator_list(message) + '\n\n Введите порядковый номер')
                    bot.register_next_step_handler(message, del_admin)
                else:
                    bot.send_message(message.from_user.id, 'Администраторов лишних нет :(')

        def del_admin(message):
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('/enter')
            markup.add(btn1)

            try:
                if Owner.objects.filter(pk=int(message.text)):
                    bot.send_message(message.from_user.id,
                                     f'Администратор под номером {int(message.text)} успешно удален',
                                     reply_markup=markup)
                    Owner.objects.filter(pk=int(message.text)).delete()
            except Exception:
                bot.send_message(message.from_user.id,
                                 'Вы допустили ошибку в номере администратора :(\n Попробуйте снова')
                bot.register_next_step_handler(message, del_admin)

        def add_admin(message):
            data = message.text.split()
            if len(data) == 4:
                Owner.objects.create(telegram_id=data[0],
                                     first_name=data[1],
                                     last_name=data[2],
                                     role=data[3])
                markup = types.ReplyKeyboardMarkup()
                btn1 = types.KeyboardButton('/enter')
                markup.add(btn1)
                bot.send_message(message.from_user.id, 'Готово!', reply_markup=markup)
            else:
                bot.send_message(message.from_user.id, 'Вы допустили ошибку')

        def work_application(message):
            """Работа над заявками"""
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('/enter')
            btn2 = types.KeyboardButton('/work')
            markup.add(btn1, btn2)
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

                bot.send_message(message.from_user.id, 'Заявка одобрена..', reply_markup=markup)
            elif message.text.lower() == 'отклонить':
                msg, _ = format_message(message)
                bot.send_message(message.from_user.id,
                                 msg + ' \n\nОТКЛОНЕНА и УДАЛЕНА ИЗ БАЗЫ ДАННЫХ!',
                                 reply_markup=markup)
                SellerApplication.objects.first().delete()

        def check_role(message):
            """Проверка ролей администраторов"""
            role = Owner.objects.get(telegram_id=message.chat.id).role
            if role in 'AO':
                if role == 'O':
                    return True, 'O'
                return True, 'A'
            else:
                return False

        def format_message(message):
            """Форматирование сообщения заявки"""
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

        def format_administrator_list(message):
            owners = Owner.objects.filter(role='A').all()
            msg = ''
            for owner in owners:
                msg += f'{owner.pk}: {owner.last_name}: {owner.first_name}\n'

            return msg

        bot.polling(none_stop=True, interval=0)
