import sys
g = ""
minp = sys.maxsize
maxp = float('-inf')
for line in sys.stdin:
    gen, price = line.strip().split('\t')
    price = float(price)
    if (gen != g and g != ""):
        print('%s\t%s\t%s'%(g,str(minp),str(maxp)))
        minp = sys.maxsize
        maxp = float('-inf')
    minp = min(price,minp)
    maxp = max(price,maxp)
    g = gen
print('%s\t%s\t%s'%(g,minp,maxp))