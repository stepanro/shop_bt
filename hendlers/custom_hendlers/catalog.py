from loader import bot
from keyboards.inline_keyboards import type_goods_keyboard, type_age_keyboard, type_size_keyboard, buy_keyboard
from state.state import UserState
from database.database import get_number_validate_goods, get_results
from telebot.types import InlineQueryResultArticle, InputTextMessageContent


@bot.message_handler(func=lambda message: message.text == '📁 Каталог')
@bot.message_handler(commands=['catalog'])
def bot_catalog(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    goods_keyboard = type_goods_keyboard()
    bot.set_state(user_id=user_id, state=UserState.catalog, chat_id=chat_id)
    text = 'Выберите раздел, чтобы вывести список товаров:'
    bot.send_chat_action(chat_id=chat_id, action=['TYPING'])
    res_send_message = bot.send_message(chat_id=chat_id, text=text,
                                        reply_markup=goods_keyboard)
    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        data['send_message_id'] = res_send_message.message_id
        data['goods_keyboard'] = goods_keyboard


@bot.callback_query_handler(func=lambda callback: callback.data.split('|')[0] == 'select_type_goods')
def select_type_goods(callback):
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        data['type_goods'] = callback.data.split('|')[1]
        message_id = data['send_message_id']
    age_keyboard = type_age_keyboard(chat_id, user_id)
    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        data['age_keyboard'] = age_keyboard
    bot.send_chat_action(chat_id=chat_id, action=['TYPING'])
    bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id,
                                  reply_markup=age_keyboard)

@bot.callback_query_handler(func=lambda callback: callback.data == 'back_to_goods')
def back_to_goods(callback):
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        message_id = data['send_message_id']
        goods_keyboard = data['goods_keyboard']
    bot.send_chat_action(chat_id=chat_id, action=['TYPING'])
    text = 'Выберите раздел, чтобы вывести список товаров:'
    bot.edit_message_text(text=text, chat_id=chat_id, message_id=message_id, reply_markup=goods_keyboard)


@bot.callback_query_handler(func=lambda callback: callback.data.split('|')[0] == 'select_type_age' or callback.data == 'back_to_goods')
def select_type_ages(callback):
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        message_id = data['send_message_id']
        data['type_age'] = callback.data.split('|')[1]
    size_keyboard = type_size_keyboard(chat_id, user_id)
    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        data['size_keyboard'] = size_keyboard
    bot.send_chat_action(chat_id=chat_id, action=['TYPING'])
    bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id,
                                  reply_markup=size_keyboard)


@bot.callback_query_handler(func=lambda query: query.data == 'back_to_age')
def back_to_age(callback):
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        message_id = data['send_message_id']
        age_keyboard = data['age_keyboard']
    bot.send_chat_action(chat_id=chat_id, action=['TYPING'])
    bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id,
                                  reply_markup=age_keyboard)


@bot.callback_query_handler(func=lambda query: query.data.split('|')[0] == 'select_type_size')
def select_type_size(callback):
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        message_id = data['send_message_id']
        data['type_size'] = callback.data.split('|')[1]

    type_goods = data['type_goods']
    type_age = data['type_age']
    type_size = data['type_size']

    number_value_goods = get_number_validate_goods(type_goods=type_goods, type_age=type_age, type_size=type_size)[0]
    bot.send_chat_action(chat_id=chat_id, action=['TYPING'])
    res_buy_keyboard = buy_keyboard()
    bot.edit_message_text(text=f'Найдено {number_value_goods} результатов, загрузите их...', chat_id=chat_id, message_id=message_id, reply_markup=res_buy_keyboard)


@bot.callback_query_handler(func=lambda callback: callback.data == 'back_to_size')
def select_type_size(callback):
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        message_id = data['send_message_id']
        size_keyboard = data['size_keyboard']
    bot.send_chat_action(chat_id=chat_id, action=['TYPING'])
    text = 'Выберите раздел, чтобы вывести список товаров:'
    bot.edit_message_text(text=text, chat_id=chat_id, message_id=message_id, reply_markup=size_keyboard)


@bot.callback_query_handler(func=lambda callback: callback.data == 'delete_search')
def select_type_size(callback):
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        message_id = data['send_message_id']
    bot.delete_message(chat_id=chat_id, message_id=message_id)


@bot.callback_query_handler(func=lambda callback: callback.data.split('|')[0] == 'download_results')
def select_type_size(callback):
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        type_goods = data['type_goods']
        type_age = data['type_age']
        type_size = data['type_size']
    res_goods = get_results(type_goods, type_age, type_size)

    for id, goods in res_goods:
        with open(file=f'picture/{id}.png', mode='rb') as document:
            bot.send_photo(chat_id=chat_id, photo=document, caption=goods)








