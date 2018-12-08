

e = []
while True:
    b = input("Сформулируйте задачу ")
    if b == "end":
        print("Выход")
        break
    c = input("Добавьте категорию к задаче ")
    d = input("Добавьте время к задаче ")
    task = [b, c, d]
    e.append (task)    
    print (task)        
print(e) 
for i in e:
    print("====")
    print("task:", i[0])
    print("cat: ", i[1])
    print("time:", i[2])
    
