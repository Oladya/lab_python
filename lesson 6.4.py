import math
a = [2,4,9,16,25]
L = [math.sqrt(c) for c in a]
print (L)



def f(x):
    return math.sqrt(x)
print (list(map(f,a)))


print(list(map(lambda x: math.sqrt(x), a)))



d=[]
for i in a:
    d.append(math.sqrt(i))
print(d)
