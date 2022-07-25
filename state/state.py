from telebot.handler_backends import State, StatesGroup


class UserState(StatesGroup):
    start_sate = State()
