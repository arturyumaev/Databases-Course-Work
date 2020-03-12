import random

out = open("./avail_male.sql", 'w')

random.seed(15)

inputs = []
for vendor in range(1, 63):
    for size in [44, 46, 48, 50, 52]:
        nsz = random.randint(3, 10)
        s = '    ({0}, {1}, {2})'.format(vendor, size, nsz)
        inputs.append(s)

head = 'insert into availability(vendor, size, number)\nvalues\n'
head += ',\n'.join(inputs)

out.write(head)
out.close()
