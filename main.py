from loader import bot
from telebot.custom_filters import StateFilter
from utils.set_default_commands import set_default_commands
import hendlers

if __name__ == '__main__':
    bot.add_custom_filter(StateFilter(bot))
    set_default_commands(bot)
    bot.polling(none_stop=True, timeout=100)
