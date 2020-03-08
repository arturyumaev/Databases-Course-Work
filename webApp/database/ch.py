f = open("./goods.csv", "r")

out = open("./goods_new.csv", "w")

data = f.readlines()

c = 0
for s in data:
    line = s.split(',')
    if c != 0:
        line[2] = line[2][23:]
        
    line[-1] = line[-1][:-1]

    
    out.write(",".join(line) + '\n')
    c += 1

out.close()
f.close()
