def test_ya(s,x):
    if s.count(x) !=0:
        return s.find(x)
    else:
        return "Not found"

def f(s):
    if (s.isalpha()) == False:
        return s.upper()

def t(s):
    if len(s) > 4:
        return s.lower()

s = "У лукоморья 123 дуб зеленый 456"
x = 'я'

print ("test_ya:", test_ya(s,x))
print (f(s))
print (t(s))

a = s[1:]
print('О' + a) 

 
