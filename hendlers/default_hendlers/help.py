from loader import bot
from config_data.config import DEFAULT_COMMANDS
from keyboards.reply_keyboards import help_keyboard


@bot.message_handler(func=lambda message: message.text == '️❓Помощь')
@bot.message_handler(commands=['help'])
def halp(message):
    chat_id = message.chat.id
    command_list = [f'/{command} - {desk}' for command, desk in DEFAULT_COMMANDS]
    bot.send_message(
        chat_id=chat_id,
        text='Список команд\n\n'+'\n'.join(command_list)+'\n\nВыберите ниже раздел справки и получите краткую помощь.',
        reply_markup=help_keyboard()
    )
