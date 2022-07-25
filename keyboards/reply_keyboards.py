from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def menu_keyboards() -> ReplyKeyboardMarkup:
    reply_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    reply_keyboards.add(
        KeyboardButton(text='📁 Каталог'),
        KeyboardButton(text='🛍 Заказы'),
        KeyboardButton(text='⚙ Настройки'),
        KeyboardButton(text='📦 Корзина'),
        KeyboardButton(text='📢 Новости'),
        KeyboardButton(text='️❓Помощь')
    )
    return reply_keyboards


def help_keyboard():
    reply_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    reply_keyboards.add(
        KeyboardButton(text='✉ Написать'),
        KeyboardButton(text='️⬅ Назад')
    )
    return reply_keyboards
