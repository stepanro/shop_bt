from loader import bot


@bot.message_handler(func=lambda message: message.text == '📢 Новости')
@bot.message_handler(commands=['news'])
def bot_news(message):
    chat_id = message.chat.id
    text = 'Это раздел НОВОСИ!'
    bot.send_message(chat_id=chat_id, text=text)