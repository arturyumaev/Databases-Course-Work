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

    def generateGetItemPrice(self, vendor):
        sqlQuery = """
        select price - (discount_bool * price * discount) from goods where vendor = {};
        """.format(vendor)

        return sqlQuery