
import json 

from tkinter import *


def read_tasks_file(filename):
    try:
        with open(filename, 'r') as f_obj:
            stat = json.load(f_obj)
        return stat
    except:
        with open (filename, 'w') as f_obj:
            pass
        return []

def save_tasks_file(filename):
     with open(filename, 'w') as f_obj:
            json.dump(e, f_obj)

def display(data):
    t1.delete(1.0, END)
    t1.insert(END, data)

def tasks_display():
    s = ""
    for i in e:
        s += "Task:{}, Category:{}, Time:{}\n".format(i["name"], i["cat"], i["time"])

    print(s)

    display(s)

def fields_clear():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')

def tasks_add():
    task= {"name":e1.get(), "cat":e2.get(), "time":e3.get()}
    e.append(task)
    print(e)
    
    save_tasks_file(fn)
    fields_clear()
    display("task added, now {}".format(len(e)))


# -----


fn = "data.task.json"
e = read_tasks_file(fn)
print(e)


master = Tk()

master.title("Task manager")

Label(master, text="Task").grid(row=0)
Label(master, text="Category").grid(row=1)
Label(master, text="Time").grid(row=2)


e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)



b1 = Button(master, text='Create', command = tasks_add)
b2 = Button(master, text='List', command = tasks_display)
b3 = Button(master, text='Exit', command=master.destroy) 


t1 = Text(master, height=15, width=50)



e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

b1.grid(row=3, column=1)
b2.grid(row=4, column=1)
b3.grid(row=5, column=1)


t1.grid(row=0, column=2, rowspan=6)




master.mainloop()


  
