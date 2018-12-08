

e = []
while True:
    b = input("Сформулируйте задачу ")
    if b == "end":
        print("Выход")
        break
    c = input("Добавьте категорию к задаче ")
    d = input("Добавьте время к задаче ")
    task= {"name":b, "cat":c, "time":d}
    e.append (task)    
    print (task)        
print(e) 
for i in e:
    print("====")
    print("name:", i["name"])
    print("cat: ", i["cat"])
    print("time:", i["time"])
    
