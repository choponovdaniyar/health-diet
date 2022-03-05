import sqlite3

class DataBase:
    def __init__(self, fn="database.db"):
        self.__connect = sqlite3.connect(fn)
        self.__cursor = self.__connect.cursor()
        self.__clear()
        self.__build()

    def __clear(self):
        self.__cursor.execute('''
            DROP TABLE products
        ''')
        self.__connect.commit()


    def __build(self):
        try:
            self.__cursor.execute('''
                CREATE TABLE products(
                    name VARCHAR(1000) ,
                    calories VARCHAR(30) DEFAULT '0',
                    proteins VARCHAR(30) DEFAULT '0',
                    fats VARCHAR(30) DEFAULT '0',
                    Carbohydrates VARCHAR(30) DEFAULT '0'
                )
            ''')
        except sqlite3.OperationalError:
            pass

    def __del__(self):
        self.__connect.close()
    

    def insert(self, row):
        try:
            self.__cursor.execute('''
                INSERT INTO products
                VALUES (?, ?, ?, ?, ?)
            ''', row)
            self.__connect.commit()
        except ValueError:
            print("недостаточно параметров")