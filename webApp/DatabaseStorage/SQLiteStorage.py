import sqlite3
from StorageInterface import StorageInterface
from Connection import Connection


class SQLiteStorage(StorageInterface):
    def __init__(self):
        self.connection = Connection(sqlite3).getInstance()
    
    def create(self, query):
        c = self.connection.cursor()
        c.execute(query)
        self.connection.commit()

    def read(self, query):
        c = self.connection.cursor()
        data = [row for row in c.execute(query)]
        self.connection.commit()

        return data

    def insertIntoCart(self, userid, vendor, size):
        insertQuery = GenerateSQLiteQueriesCart().generateInsertIntoCart(userid, vendor, size)
        self.create(insertQuery)
        self.getItemsAmount(userid)

    def getItemsAmount(self, userid):
        selectQuery = GenerateSQLiteQueriesCart().generateGetCartItemsAmount(userid)
        data = self.read(selectQuery)
        goodsAmount = [_ for _ in data][0][0]

        return goodsAmount
        
    def getData(self, gender, sortby, cats):
        selectQuery = GenerateSQLiteQueriesGoods().generateGetGoods(gender, sort_by, cats)
        self.read(selectQuery)

    def selectCart(self, userid):
        selectQuery = GenerateSQLiteQueriesCart().generateGetCart(userid)
        self.read(selectQuery)

    def update(self):
        pass

    def delete(self):
        pass

class GenerateSQLiteQueriesCart():
    def __init__(self):
        pass

    def generateInsertIntoCart(self, userid, vendor, size):
        sqlQuery = """
        insert into cart (userid, vendor, size) values
        (\'{}\',{},{});
        """.format(userid, vendor, size)

        return sqlQuery

    def generateGetCartItemsAmount(self, userid):
        sqlQuery = """
        select count(userid) from cart where userid = '{}';
        """.format(userid)

        return sqlQuery

    def generateGetCart(self, userid):
        sqlQuery = """
        select *, count(*) as amount from (
            select g.description,
                g.category,
                g.gender,
                c.size,
                g.color,
                g.price * (1 - g.discount) as price,
                c.vendor
            from cart c
            join goods g
            on c.vendor = g.vendor
            where userid = '{0}'
        ) as items
        group by vendor, size
        having count(*) >= 1
        """.format(userid)

        return sqlQuery

class GenerateSQLiteQueriesGoods():
    def __init__(self):
        pass

    def generateGetGoods(self, gender, sort_by, cats):
        sqlQuery = 'select * from goods'
        if gender != 'forall':
            sqlQuery += ' where gender = \'{}\''.format(gender)

        if cats != 'None' and cats != ['None']:
            if gender == 'forall':
                sqlQuery += (' where (' + " or ".join(['category = \'{}\''.format(cat) for cat in cats]) + ')')
            else:
                sqlQuery += (' and (' + " or ".join(['category = \'{}\''.format(cat) for cat in cats]) + ')')

        sqlQuery += ' order by '
        if sort_by == 'By popularity' or sort_by == 'Sort by':
            sqlQuery += 'rating desc'
        if sort_by == 'Ascending prices':
            sqlQuery += 'price'
        if sort_by == 'Descending prices':
            sqlQuery += 'price desc'

        return sqlQuery
