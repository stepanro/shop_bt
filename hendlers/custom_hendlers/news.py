from loader import bot


@bot.message_handler(func=lambda message: message.text == '📢 Новости')
@bot.message_handler(commands=['news'])
def bot_news(message):
    pass