


import random 

s = ["самовар","весна", "лето"]

a = random.randint(0, len(s)-1)
b = random.randint(0, len(s[a]) - 1)

print (s[a][0:b] + "?" + s[a][b+1: ])

x = input ("Введите букву: ")

def check (x):
    if x == s[a][b]:
        return "Победа"
    else:
        return "Увы! Попробуйте в другой раз!"

print (check(x))
