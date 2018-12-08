
s = input("Введите чиcло")
total = 0
for i in range(len(s)):
    if i%2 == 1:
        total = total + (int(s[i]))**2
print ("сумма квадратов цифр:", total)
