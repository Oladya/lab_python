s = "У лукоморья 123 дуб зеленый 456"

print (s.count ("я"))
print (s.find ("я"))
print (s.find ("у"))
def f(s):
    if (s.isalpha()) == False:
        print (s.upper())    
f(s)
a = len(s)
if a > 4:
    print (s.lower())


print (s.replace(s[0], "О"))


 
