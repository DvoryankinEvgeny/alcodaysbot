import telebot
import config
import database
import alcodaysbot

if __name__ == "__main__":
    telegram = telebot.TeleBot(config.token)
    db = database.Database('mongo', 27017)
    bot = alcodaysbot.AlcoBot(telegram, db)
    bot.run()
