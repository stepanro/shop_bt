from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.database import get_type_goods, get_age, get_size, get_results
from loader import bot


def type_goods_keyboard():
    """ Функция возвращает клавиатуру с товарами в зависимости от стадии выбора товара """
    type_goods = get_type_goods()
    inline_keyboard = InlineKeyboardMarkup(row_width=2)
    inline_keyboard.add(*[InlineKeyboardButton(text=type, callback_data=f'select_type_goods|{type}') for type in type_goods])
    inline_keyboard.add(InlineKeyboardButton(text='🌟 Избранное', callback_data='favorites'))
    return inline_keyboard


def type_age_keyboard(chat_id, user_id):
    """ Функция возвращает клавиатуру с вариантами возрастных типов """
    with bot.retrieve_data(chat_id=chat_id, user_id=user_id) as data:
        type_goods = data['type_goods']
    type_age = get_age(type_goods=type_goods)
    inline_keyboard = InlineKeyboardMarkup(row_width=2)

    inline_keyboard.add(*[InlineKeyboardButton(text=type, callback_data=f'select_type_age|{type}') for type in type_age])
    inline_keyboard.add(InlineKeyboardButton(text='Назад', callback_data=f'back_to_goods'))
    return inline_keyboard


def type_size_keyboard(chat_id, user_id):
    """ Функция возвращает клавиатуру с вариантами размерных типов """
    with bot.retrieve_data(chat_id=chat_id, user_id=user_id) as data:
        type_goods, type_age = data['type_goods'], data['type_age']
    type_size = get_size(type_goods=type_goods, type_age=type_age)
    inline_keyboard = InlineKeyboardMarkup(row_width=2)
    inline_keyboard.add(*[InlineKeyboardButton(text=type, callback_data=f'select_type_size|{type}') for type in type_size],)
    inline_keyboard.add(
                        InlineKeyboardButton(text='Назад', callback_data='back_to_age'),
                        InlineKeyboardButton(text='В начало каталога', callback_data='back_to_goods')
                        )
    return inline_keyboard


def buy_keyboard(chat_id, user_id):
    """ Функция возвращает клавиатуру для покупки товара """
    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        type_goods = data['type_goods']
        type_age = data['type_age']
        type_size = data['type_size']

    inline_keyboard = InlineKeyboardMarkup(row_width=2)
    inline_keyboard.add(InlineKeyboardButton(text='Загрузить результаты?', switch_inline_query_current_chat=f'load|{type_goods}|{type_age}|{type_size}'))
    inline_keyboard.add(
                        InlineKeyboardButton(text='Назад', callback_data='back_to_size'),
                        InlineKeyboardButton(text='В начало каталога', callback_data='back_to_goods')
                        )
    inline_keyboard.add(InlineKeyboardButton(text='Удалить поиск', callback_data='delete_search'))

    return inline_keyboard


def clarifying_keyboard():
    inline_keyboard = InlineKeyboardMarkup(row_width=3)
    inline_keyboard.add(InlineKeyboardButton(text='Купить', callback_data='buy'))
    inline_keyboard.add(
                        InlineKeyboardButton(text='➖', callback_data='➖'),
                        InlineKeyboardButton(text='1 шт.', callback_data='1 шт.'),
                        InlineKeyboardButton(text='➕', callback_data='➕')
                        )
    inline_keyboard.add(InlineKeyboardButton(text='Добавить в избранное', callback_data='Добавить в избранное'))
    inline_keyboard.add(InlineKeyboardButton(text='Корзина', callback_data='Корзина'))

    return inline_keyboard
