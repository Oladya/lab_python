dict_pizza = {
    'pepperoni': {'consist': ("pepperoni","mozarella","tomato sauce"), 'size_price':{'s':395, 'm':545}},
    'margarita': {'consist': ("Tomato","mozarella","tomato sauce"), 'size_price':{'s':395, 'm':545}},
    'Hawaiian': {'consist': ("Chicken","ham","pineapple", "mozarella","tomato sauce"), 'size_price':{'s':415, 'm':595}}

}

print( dict_pizza["Hawaiian"]["consist"])
print( dict_pizza["Hawaiian"]['size_price']['m'])


