from loader import bot


@bot.message_handler(commands=['about_project'])
def bot_about_project(message):
    chat_id = message.chat.id
    text = 'Платформа для продажи. По всем вопросам пишите на почту mail@stevenhorn.ru'
    bot.send_message(chat_id=chat_id, text=text)
    