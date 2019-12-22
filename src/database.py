from pymongo import MongoClient


class Database:
    def __init__(self, ip, port):
        self.__client = MongoClient(ip, port)
        self.__db = self.__client.alcodaysbot

    def isDateExist(self, user_id, date):
        rec = self.__db.records.find_one({'user_id': user_id, 'drink_date': date})
        if rec:
            return True

        return False

    def insert(self, user_id, date):
        message = {'user_id': user_id, 'drink_date': date}        
        self.__db.records.insert_one(message)

    def findAll(self, user_id):
        records = self.__db.records.find({'user_id': user_id})
        dates = []
        for r in records:
            print(r['drink_date'])
            dates.append(r['drink_date'])

        return dates
