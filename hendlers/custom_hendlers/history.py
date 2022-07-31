from loader import bot


@bot.message_handler(func=lambda message: message.text == '🛍 Заказы')
@bot.message_handler(commands=['history'])
def bot_history(message):
    pass