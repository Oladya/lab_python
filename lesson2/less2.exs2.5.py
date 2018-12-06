


def cost (a, y):
    if a == 343:
        b = 15
        return  b*y
    if a == 381:
        b = 18
        return  b*y
    if a == 473:
        b = 13
        return  b*y
    if a == 485:
        b = 11
        return  b*y
    else:
        return "unknown code"

a = int (input ('city code'))
y = int (input ('time'))
print (cost (a,y))

      
    

