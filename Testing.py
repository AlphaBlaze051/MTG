import ast
from tkinter import *
 

root = Tk()
root.title("Testing")
root.geometry('350x200')
 
lbl = Label(root, text = "Are you a Geek?")
lbl.grid()
 
txt = Entry(root, width=10)
txt.insert(0, 'CardInfo')
txt.grid(column =1, row =0)

def clicked():
    test=txt.get()
    if test != 'CardInfo':
        file = open(test+".py", "r")
    elif test == 'CardInfo':
        file = open("test.txt", "r")
    Cards = ast.literal_eval(file.read())
    file.close()
    print(type(Cards))
    for d in Cards.values():
        if  d['CardName']=='Abandon Hope':
            print(d['CardName'])

btn = Button(root, text = "Click me" , command=clicked)
btn.grid(column=2, row=0)
 
root.mainloop()

