import sqlite3


def insert_into_cart(userid, vendor, size):
    conn = sqlite3.connect('./database/catalog.db')
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
    conn = sqlite3.connect('./database/catalog.db')
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
