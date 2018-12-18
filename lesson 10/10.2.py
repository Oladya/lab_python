
import random
import tkinter

a = {"dog":"собака", "cat":"кошка", "mouse": "мышь"}

b = random.choice(list(a.keys()))

def click():
    if a[b] == entry.get():
        label.config(text = "Угадали")
    else:
        label.config(text = "Не угадали")
    
window = tkinter.Tk()
label = tkinter.Label (window, text = "Случайное слово:")
label.pack()

label4 = tkinter.Label (window, text =b)
label4.pack()


label2 = tkinter.Label (window, text = "Укажите перевод слова:")
label2.pack()


entry = tkinter.Entry(window)
entry.pack()


label = tkinter.Label(window)
label.pack()

button2 = tkinter.Button(window, text='Готово', command=click) 
button2.pack()


button1 = tkinter.Button(window, text='Выход', command=window.destroy) 
button1.pack()

window.mainloop()



