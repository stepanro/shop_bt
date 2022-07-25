from loader import bot
from keyboards.reply_keyboards import menu_keyboards


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    user_name = message.from_user.full_name
    bot.send_message(chat_id=chat_id, text=f'Здравствуйте {user_name}', reply_markup=menu_keyboards())
