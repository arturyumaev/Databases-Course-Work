import sys
sys.path.insert(0,'..')

from DatabaseStorage.StorageInterface import StorageInterface
from DatabaseStorage.SQLiteQuery.generateSQLiteQueriesCart import GenerateSQLiteQueriesCart
from DatabaseStorage.SQLiteQuery.generateSQLiteQueriesGoods import GenerateSQLiteQueriesGoods
from DatabaseStorage.SQLiteQuery.generateSQLiteQueriesAvailability import GenerateSQLiteQueriesAvailability
from DatabaseStorage.SQLiteQuery.generateSQLiteQueriesOrders import GenerateSQLiteQueriesOrders
from Connection import Connection

class SQLiteStorage(StorageInterface):
    def connect(self):
        self.connection = Connection().getInstance()
    
    def create(self, query):
        self.connect()
        c = self.connection.cursor()
        c.execute(query)
        self.connection.commit()
        self.connection.close()

    def read(self, query):
        self.connect()
        c = self.connection.cursor()
        data = [row for row in c.execute(query)]
        self.connection.commit()
        self.connection.close()

        return data

    def insertIntoCart(self, userid, vendor, size):
        insertQuery = GenerateSQLiteQueriesCart().generateInsertIntoCart(userid, vendor, size)
        self.create(insertQuery)

    def getItemsAmount(self, userid):
        selectQuery = GenerateSQLiteQueriesCart().generateGetCartItemsAmount(userid)
        data = self.read(selectQuery)
        goodsAmount = [_ for _ in data][0][0]

        return goodsAmount

    def getItemsQuantity(self):
        selectQuery = GenerateSQLiteQueriesAvailability().generateGetItemsQuantity()
        data = self.read(selectQuery)
        itemsQuantity = [item[1:] for item in data]

        itemsAvailabilityDictionary = {}
        for t in itemsQuantity:
            if t[0] in itemsAvailabilityDictionary: # t[0] - vendor
                itemsAvailabilityDictionary[t[0]][t[1]] = t[2]
            else:
                itemsAvailabilityDictionary[t[0]] = {t[1]: t[2]}

        return itemsAvailabilityDictionary
        
    def getData(self, gender, sort_by, cats):
        selectQuery = GenerateSQLiteQueriesGoods().generateGetGoods(gender, sort_by, cats)
        data = self.read(selectQuery)

        return data

    def selectCart(self, userid):
        selectQuery = GenerateSQLiteQueriesCart().generateGetCart(userid)
        data = self.read(selectQuery)

        return data

    def getItemPrice(self, vendor):
        selectQuery = GenerateSQLiteQueriesGoods().generateGetItemPrice(vendor)
        data = self.read(selectQuery)

        return data

    def update(self):
        pass

    def delete(self):
        pass
