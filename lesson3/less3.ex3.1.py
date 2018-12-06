

a = int(input ("a = "))
b = int(input ("b = "))
c = int(input ("c = "))
def geron(a, b, c):
    p=(a+b+c)/2
    print( (p*(p-a)*(p-b)*(p-c))**0.5)
  
geron(a,b,c)
