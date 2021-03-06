import datetime

class AlcoBot:
    def __init__(self, bot, db):
        self.__bot = bot
        self.__db = db

        self.__welcome_msg = """Hi, {}. I will store dates when you drank
        /today - to add today to your drink dates
        /yesterday - to add yesterday to your drink dates
        /add - add new drink date in format YYYY-MM-DD
        /show - show all drink dates
        """

        self.__bot.add_message_handler({
            'function': self.__send_welcome,
            'filters': {'commands': ['start', 'help']}
        })

        self.__bot.add_message_handler({
            'function': self.__add_new_date,
            'filters': {'commands': ['add']}
        })

        self.__bot.add_message_handler({
            'function': self.__show_alco_dates,
            'filters': {'commands': ['show']}
        })

        self.__bot.add_message_handler({
            'function': self.__add_today,
            'filters': {'commands': ['today']}
        })

        self.__bot.add_message_handler({
            'function': self.__add_yesterday,
            'filters': {'commands': ['yesterday']}
        })

    def run(self):
        self.__bot.polling(none_stop=True)

    def __insert_date(self, message, date):
        if not self.__db.isDateExist(message.from_user.id, date):
            self.__db.insert(message.from_user.id, date)
            self.__bot.reply_to(message, "Added")
        else:
            self.__bot.reply_to(message, "Already exist")

    def __send_welcome(self, message):
        self.__bot.reply_to(message, self.__welcome_msg.format(
            message.from_user.username))

    def __add_new_date(self, message):
        parts = str(message.text).split(' ',maxsplit=1)
        self.__insert_date(message, parts[1])

    def __add_today(self, message):
        now = datetime.datetime.today().strftime("%Y-%m-%d")
        self.__insert_date(message, now)

    def __add_yesterday(self, message):
        now = datetime.datetime.today()
        yesterday = now - datetime.timedelta(days=1)
        self.__insert_date(message, yesterday.strftime("%Y-%m-%d"))

    def __show_alco_dates(self, message):
        dates = self.__db.findAll(message.from_user.id)
        self.__bot.reply_to(message, str(dates))
