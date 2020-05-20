class GenerateSQLiteQueriesOrders:
    def __init__(self):
        pass

    def generateInsertIntoOrders(self, orderNumber, cartId, name, vendor, size, quantity, email, time):
        sqlQuery = """
        insert into orders (orderNumber, cartId, name, vendor, size, quantity, email, time)
            values
                ('{}', '{}', '{}', {}, {}, {}, '{}', '{}');
        """.format(orderNumber, cartId, name, vendor, size, quantity, email, time)

        return sqlQuery

