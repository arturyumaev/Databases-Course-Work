import sqlite3

def make_sql_query(gender, sort_by, cats):

    # Create database for catalog of clothing
    conn = sqlite3.connect('./database/catalog.db')
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
