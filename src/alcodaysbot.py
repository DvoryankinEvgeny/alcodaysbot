import telebot
import config

class AlcoBot:
    def __init__(self):
        self.bot = telebot.TeleBot(config.token)
        self.bot.add_message_handler({
            'function': self.send_welcome,
            'filters': {'commands':['start', 'help']}
        })

    def run(self):
        self.bot.polling()

    def send_welcome(self, message):
        self.bot.reply_to(message, "{}, how are you doing?".format(message.from_user.username))

    