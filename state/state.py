from telebot.handler_backends import State, StatesGroup


class UserState(StatesGroup):
    """catalog state"""
    select_type_goods = State()
    select_type_ages = State()
    select_type_size = State()
    bot_inline_handler_load = State()
    load = State()

