import random

out = open("./male.sql", 'w')

random.seed(15)
string = """
insert into goods (vendor, gender, photo, rating, price, discount, discount_bool, new, description, category, color)\nvalues\n"""
out.write(string)
for i in range(1, 63):
    vendor = '{:04d}'.format(i)
    cat = ""
    price = 0
    if i <= 10:
        cat = 'accessories'
        price = random.randint(2000, 4500)
    if i > 10 and i <= 26:
        cat = 'outerwear'
        price = random.randint(10000, 45000)
    if i > 26 and i <= 42:
        cat = 'pants'
        price = random.randint(4000, 8000)
    if i > 42 and i <= 52:
        cat = 'shoes'
        price = random.randint(4000, 7000)
    if i > 52 and i <= 62:
        cat = 'tshirts'
        price = random.randint(2000, 2500)
    path = '/database/img/catalog/men/' + cat + '/' + str(vendor) + '.jpg'
    rating = random.randint(0, 100)
    s = '    ({}, \'{}\', \'{}\', {}, {}, , , , , \'{}\', ),\n'.format(vendor, 'male', path, rating, price, cat)

    out.write(s)

out.close()    
