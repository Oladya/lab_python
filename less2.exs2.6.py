
def costFri(t):
    pr = 0
    if t == 12:
        pr = 250
    if t == 16:
        pr = 350
    if t == 20:
        pr = 450
    return pr

def costChamp(t):
    pr = 0
    if t == 10:
        pr = 250
    if t == 13:
        pr = 350
    if t == 16:
        pr = 350
    return pr

def costBird(t):
    pr = 0
    if t == 10:
        pr = 350
    if t == 14:
        pr = 450
    if t == 18:
        pr = 450
    return pr


film = input ("name of film:")
date = input("date of film:")
time = int (input ("time of film:"))
number = int (input ("number of tickets:"))


price = 0

if film == "Friday":
    price = number * costFri(time)

if film == "Champions":
    price = number * costChamp(time)


if film == "Bird":
    price = number * costBird(time)


if number >= 20:
    price = price * 0.8

if date == "today":s
    price = price * 0.95

print(price)




