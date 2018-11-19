value = int(input('Enter the atomic number of the element:'))

def f(y):
    if y  == 3:
        return "Lithium"
    elif y  == 25:
        return "Manganum"
    elif y  == 80:
        return "Hydrargyrum"
    elif y  == 17:
        return "Chlorum"
    else:
        return "What' it?")
print (f(value))

