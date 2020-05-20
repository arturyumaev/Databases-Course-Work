class GenerateSQLiteQueriesAvailability():
    def __init__(self):
        pass

    def generateGetItemsQuantity(self):
        sqlQuery = "select * from availability;"

        return sqlQuery
    
    def generateUpdateItemQuantity(self, vendor, size, orderedQuantity):
        sqlQuery = """
        update availability
        set number = number - {}
        where vendor = {} and size = {};
        """.format(orderedQuantity, vendor, size)

        return sqlQuery