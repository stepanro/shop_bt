import time
from loader import bot


def delete_echo_message(chat_id, output_message_id, input_message_id, text_message, start_time_delete_message):
    for sec in range(start_time_delete_message - 1, 0, -1):
        time.sleep(1)
        bot.edit_message_text(text=f'Ваше сообщение "{text_message}" не содержит команду, оно будет удалено через {sec} секунд', chat_id=chat_id, message_id=output_message_id)
    bot.delete_message(chat_id=chat_id, message_id=input_message_id)
    bot.delete_message(chat_id=chat_id, message_id=output_message_id)


@bot.message_handler(state=None)
def bot_echo(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    start_time_delete_message = 10
    text_message = message.text
    input_message_id = message.id
    send_message = bot.send_message(chat_id=chat_id, text=f'Ваше сообщение "{text_message}" не содержит команду, оно будет удалено через {start_time_delete_message} секунд')
    output_message_id = send_message.id
    delete_echo_message(chat_id=chat_id, output_message_id=output_message_id, input_message_id=input_message_id, text_message=text_message, start_time_delete_message=start_time_delete_message)
