import math
a = [2,4,9,16,25]
L = [math.sqrt(c) for c in a]
print (L)


print (list(map(math.sqrt,a)))


d=[]
for i in a:
    d.append(math.sqrt(i))
print(d)
