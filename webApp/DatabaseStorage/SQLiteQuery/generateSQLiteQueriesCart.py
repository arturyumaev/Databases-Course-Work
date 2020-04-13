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