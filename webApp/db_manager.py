import sqlite3
from StorageInterface import StorageInterface


class DatabaseStorage(StorageInterface):
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

    def update(self):
        pass

    def delete(self):
        pass    



# Cart table
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

# Goods table
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

# Connection
class Connection:
    def __init__(self, server):
        self.server = server
        self.instance = None
        self.configuration = None
    
    def getInstance(self):
        if self.server.__name__ == "sqlite3":

            with open("./db.conf", "r") as sqliteConfig:
                self.configuration = sqliteConfig.readline()
            
            try:
                self.instance = self.server.connect(self.configuration)

                return self.instance
            except IOError:
                print('An error occurred trying to connect to sqlite3')
        else:
            # Handling of other database servers may be added
            return None





with open("./db.conf", "r") as database_config:
    DB_PATH = database_config.readline()

def insert_into_cart(userid, vendor, size):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    sql_query = 'insert into cart (userid, vendor, size) values '
    sql_query += '(\'{}\',{},{});'.format(userid, vendor, size)

    print(sql_query)

    c.execute(sql_query)
    conn.commit()

    goods_amount = c.execute("select count(userid) from cart where userid = '{}';".format(userid))
    goods_amount = [i for i in goods_amount][0][0]

    conn.close()

    return goods_amount

def get_items_amount(userid):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    goods_amount = c.execute("select count(userid) from cart where userid = '{}';".format(userid))
    goods_amount = [i for i in goods_amount][0][0]

    conn.close()

    return goods_amount

def get_data(request):
    url_args = list(request.args.keys())
    if all(i in url_args for i in ['sort', 'gender', 'cats']):
        sort_by = request.args.get('sort')
        gender = request.args.get('gender')
        categories = request.args.getlist('cats')
    else:
        sort_by = 'Sort by'
        gender = 'forall'
        categories = 'None'

    data = make_sql_query(gender, sort_by, categories)

    return data

def make_sql_query(gender, sort_by, cats):

    # Create database for catalog of clothing
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    sql_query = 'select * from goods'
    if gender != 'forall':
        sql_query += ' where gender = \'{}\''.format(gender)

    if cats != 'None' and cats != ['None']:
        if gender == 'forall':
            sql_query += (' where (' + " or ".join(['category = \'{}\''.format(cat) for cat in cats]) + ')')
        else:
            sql_query += (' and (' + " or ".join(['category = \'{}\''.format(cat) for cat in cats]) + ')')

    sql_query += ' order by '
    if sort_by == 'By popularity' or sort_by == 'Sort by':
        sql_query += 'rating desc'
    if sort_by == 'Ascending prices':
        sql_query += 'price'
    if sort_by == 'Descending prices':
        sql_query += 'price desc'

    print(sql_query)
    data = [i for i in c.execute(sql_query)]

    conn.close()

    return data

def select_cart(userid):
    sql_query = """
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

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    data = [i for i in c.execute(sql_query)]
    conn.close()

    return data
