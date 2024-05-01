Python 3.12

pip3 -r install requirements


Create file .env

PS
Проверка функциональности можно проверить через SQLite3, но желательно пользоваться MySQL


.env:
# Settings marketplace .env

DEBUG = True
SECRET_KEY =        # Сгенерируйте секретный ключ
NAME =              # Создайте БД в mysql
USER =              # Имя пользователя БД
PASSWORD =          # Пароль пользователя БД
HOST = localhost    # Хост по умолчанию
PORT = 3306         # *Порт по умолчанию