import os
from dotenv import load_dotenv, find_dotenv
from loguru import logger
from datetime import datetime

""" Проверяем наличие файла .env, если файл есть, инициализируем переменные окружения """
if not find_dotenv():
    logger.info(f'{datetime} файл ".env" не найден, создайте и заполните файл ".env" по образцу файла ".env.template"')
else:
    load_dotenv()


""" Инициализируем logger """
logger.add('debug.log', format='{time} {level} {message}', level='DEBUG')


""" Инициализируем переменные окружения """
BOT_TOKEN = os.getenv('BOT_TOKEN')


""" Инициализируем данные базы данных """
HOST_NAME = os.getenv('HOST_NAME')
HOST_USER_NAME = os.getenv('HOST_USER_NAME')
PASSWORD = os.getenv('PASSWORD')
NAME_DATABASE = os.getenv('NAME_DATABASE')


""" Инициализируем команды бота """
DEFAULT_COMMANDS = (
    ('start', 'Главное меню'),
    ('catalog', 'Каталог'),
    ('cart', 'Корзина'),
    ('history', 'История заказов'),
    ('news', 'Наши новости и акции'),
    ('setting', 'Настройки'),
    ('help', 'Справка'),
    ('about_project', 'О проекте')
)
