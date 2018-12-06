


import random
a = random.randint(0,100)
g = random.randint(1,5)
print ("Число попыток", g)
number_of_guesses = 0
while number_of_guesses < g:
    b = input("Попробуйте угадать или введите Выход для остановки программы: ") 
    number_of_guesses = number_of_guesses + 1
    if b == "Выход":
        print("Выход из программы! До встречи!")
        break
    elif a > int(b):
        print("Попробуйте число больше")
    elif a < int(b):
        print("Попробуйте число меньше")
    else:
        print ("Победа!")
		break

if number_of_guesses == g:
    print("Игра окончена", "Загаданное число", a)







    
