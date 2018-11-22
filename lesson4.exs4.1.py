
x = int(input ("x= "))
def f(x):
    if 0 < x < 10:
         print ('{x:.1f}'.format(x=22/7))
    elif 10 < x < 100:
        print ('{x:.2f}'.format(x=22/7))
    elif 100 < x < 1000:
        print ('{x:.3f}'.format(x=22/7))
    else:
        print ('{x:.4f}'.format(x=22/7))
f(x)
