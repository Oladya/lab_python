import json 
def read_tasks_file(filename):
    try:
        with open(filename, 'r') as f_obj:
            stat = json.load(f_obj)
        return stat
    except IOError:
        with open (filename, 'w') as f_obj:
            pass
        return []
filename= "task.json"
e = read_tasks_file(filename)
print(e)
while True:
    b = input("Сформулируйте задачу ")
    if b == "end":    
        with open(filename, 'w') as f_obj:
            json.dump(e, f_obj)
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
    
