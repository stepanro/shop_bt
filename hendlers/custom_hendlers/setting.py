from loader import bot


@bot.message_handler(func=lambda message: message.text == '⚙ Настройки')
@bot.message_handler(commands=['setting'])
def bot_setting(message):
    pass
