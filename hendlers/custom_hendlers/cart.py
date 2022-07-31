from loader import bot


@bot.message_handler(func=lambda message: message.text == '📦 Корзина')
@bot.message_handler(commands=['cart'])
def bot_cart(message):
    pass