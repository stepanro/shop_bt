from telebot.handler_backends import State, StatesGroup


class UserState(StatesGroup):
    """catalog state"""
    catalog = State()

