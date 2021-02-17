from tkinter import *
from CardInfo import cards 
from mergedeep import merge
import ast
import pickle

allcards={}
rarity1=['Rarity', 'Rare', 'Uncommon', 'Common', 'Mythic Rare', 'Bonus', 'Special', 'Promo']
types=['Type','Enchantment', 'Creature', 'Sorcery', 'Instant', 'Land', 'Artifact', 'Planeswalker', 'Artifact Creature', 'Enchantment Creature', 'Tribal Sorcery', 'Artifact Land', 'Enchantment Artifact', 'Tribal Enchantment', 'Tribal Instant', 'Tribal Artifact', 'Land Creature', 'Enchantment Land', 'Instant Creature']
mana=['Color','R','B','U','W','G']
mana2=['Color','Red','Black','Blue','White','Green']


master = Tk()
master.title('GUI Test')
master.geometry('450x300')

frame = Frame(master) 
frame.pack()

menubar = Menu(master)

def filter():
    for widget in frame.winfo_children():
        widget.destroy()

    #Rarity Drop Down
    variable1 = StringVar(frame)
    variable1.set(rarity1[0]) # default value
    w1 = OptionMenu(frame, variable1, *rarity1)
    w1.grid(row = 0, column = 2, pady = 2)
    l1 = Label(frame, text = "Rarity:") 
    l1.grid(row = 0, column = 1, pady = 2)

    #Type Drop Down
    variable2 = StringVar(frame)
    variable2.set(types[0]) # default value
    w2 = OptionMenu(frame, variable2, *types)
    w2.grid(row = 1, column = 2, pady = 2)
    l2 = Label(frame, text = "Type:") 
    l2.grid(row = 1, column = 1, pady = 2)

    #Mana Drop Down
    variable3 = StringVar(frame)
    variable3.set(mana[0]) # default value
    w3 = OptionMenu(frame, variable3, *mana2 )
    w3.grid(row = 2, column = 2, pady = 2)
    l5 = Label(frame, text = "Mana:") 
    l5.grid(row = 2, column = 1, pady = 2)

    #Power text box
    w4 = Entry(frame, width=10)
    w4.grid(row = 3, column = 2, pady = 2)
    w4.insert(0, "Power")
    l4 = Label(frame, text = "Power:") 
    l4.grid(row = 3, column = 1, pady = 2)

    #Toughness text box
    w5 = Entry(frame, width=10)
    w5.grid(row = 4, column = 2, pady = 2)
    w5.insert(0, "Toughness")
    l5 = Label(frame, text = "Toughness:") 
    l5.grid(row = 4, column = 1, pady = 2)

    #File Text Box
    w6 = Entry(frame, width=10)
    w6.grid(row = 5, column = 2, pady = 2)
    w6.insert(0, "CardInfo")
    l6 = Label(frame, text = "File Name:") 
    l6.grid(row = 5, column = 1, pady = 2)
    

    listbox = Listbox(frame, height = 15,  
                    width = 30,  
                    bg = "light grey", 
                    activestyle = 'dotbox',  
                    font = "Helvetica", 
                    fg = "black") 
    listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 7, padx = 5, pady = 5)

    def Reset():
        variable1.set(rarity1[0])
        variable2.set(types[0])
        variable3.set(mana[0])
        w4.delete(0,END)
        w4.insert(0,'Power')
        w5.delete(0,END)
        w5.insert(0,'Toughness')
        w6.delete(0,END)
        w6.insert(0,'CardInfo')
        ok()
    
    def ok():
        test=w6.get()
        if test != 'CardInfo':
            file = open(test+".py", "r")
        elif test == 'CardInfo':
            file = open("test.txt", "r")
        Cards = ast.literal_eval(file.read())
        file.close()

        mana3=mana2.index(variable3.get())
        listbox.delete(0, listbox.size())
        mana3=mana2.index(variable3.get())
        listbox.delete(0, listbox.size())
        if variable1.get() != 'Rarity' and variable2.get() !='Type' and mana[mana3] !='Color' and 'Power'!=w4.get() and 'Toughness'!=w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['Rarity'] == variable1.get() and d['CardType']==variable2.get() and mana[mana3] in d['Mana'] and CPT2[0]==w4.get() and CPT2[1]==w5.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done rarity, type, color, power and toughness')

        elif variable1.get() != 'Rarity' and variable2.get() !='Type' and mana[mana3] !='Color' and 'Power'!=w4.get() and 'Toughness'==w5.get():
            for d in Cards.values(): 
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['Rarity'] == variable1.get() and d['CardType']==variable2.get() and mana[mana3] in d['Mana'] and CPT2[0]==w4.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done rarity, type, color and power')

        elif variable1.get() != 'Rarity' and variable2.get() !='Type' and mana[mana3] !='Color' and 'Power'==w4.get() and 'Toughness'!=w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['Rarity'] == variable1.get() and d['CardType']==variable2.get() and mana[mana3] in d['Mana'] and CPT2[1]==w5.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done rarity, type, color and toughness')

        elif variable1.get() != 'Rarity' and variable2.get() !='Type' and mana[mana3] =='Color' and 'Power'!=w4.get() and 'Toughness'!=w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['Rarity'] == variable1.get() and d['CardType']==variable2.get() and CPT2[0]==w4.get() and CPT2[1]==w5.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done rarity, type, power and toughness')

        elif variable1.get() != 'Rarity' and variable2.get() =='Type' and mana[mana3] !='Color' and 'Power'!=w4.get() and 'Toughness'!=w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['Rarity'] == variable1.get() and mana[mana3] in d['Mana'] and CPT2[0]==w4.get() and CPT2[1]==w5.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done rarity, color, power and toughness')

        elif variable1.get() == 'Rarity' and variable2.get() !='Type' and mana[mana3] !='Color' and 'Power'!=w4.get() and 'Toughness'!=w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['CardType']==variable2.get() and mana[mana3] in d['Mana'] and CPT2[0]==w4.get() and CPT2[1]==w5.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done type, color, power and toughness')

        elif variable1.get() != 'Rarity' and variable2.get() !='Type' and mana[mana3] !='Color' and 'Power'==w4.get() and 'Toughness'==w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['Rarity'] == variable1.get() and d['CardType']==variable2.get() and mana[mana3] in d['Mana']:
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done rarity, type, color, power and toughness')

        elif variable1.get() != 'Rarity' and variable2.get() !='Type' and mana[mana3] =='Color' and 'Power'!=w4.get() and 'Toughness'==w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['Rarity'] == variable1.get() and d['CardType']==variable2.get() and CPT2[0]==w4.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done rarity, type and power ')
        
        elif variable1.get() != 'Rarity' and variable2.get() !='Type' and mana[mana3] =='Color' and 'Power'==w4.get() and 'Toughness'!=w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['Rarity'] == variable1.get() and d['CardType']==variable2.get() and CPT2[1]==w5.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done rarity, type and Toughness')

        elif variable1.get() != 'Rarity' and variable2.get() =='Type' and mana[mana3] !='Color' and 'Power'!=w4.get() and 'Toughness'==w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['Rarity'] == variable1.get() and mana[mana3] in d['Mana'] and CPT2[0]==w4.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done rarity, color and power')

        elif variable1.get() != 'Rarity' and variable2.get() =='Type' and mana[mana3] !='Color' and 'Power'==w4.get() and 'Toughness'!=w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['Rarity'] == variable1.get() and mana[mana3] in d['Mana'] and CPT2[1]==w5.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done rarity, color and toughness')

        elif variable1.get() != 'Rarity' and variable2.get() =='Type' and mana[mana3] =='Color' and 'Power'!=w4.get() and 'Toughness'!=w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['Rarity'] == variable1.get() and CPT2[0]==w4.get() and CPT2[1]==w5.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done rarity, power and toughness')

        elif variable1.get() == 'Rarity' and variable2.get() !='Type' and mana[mana3] !='Color' and 'Power'!=w4.get() and 'Toughness'==w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['CardType']==variable2.get() and mana[mana3] in d['Mana'] and CPT2[0]==w4.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done type, color and power')

        elif variable1.get() == 'Rarity' and variable2.get() !='Type' and mana[mana3] !='Color' and 'Power'==w4.get() and 'Toughness'!=w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['CardType']==variable2.get() and mana[mana3] in d['Mana'] and CPT2[1]==w5.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done type, color and toughness')

        elif variable1.get() == 'Rarity' and variable2.get() =='Type' and mana[mana3] !='Color' and 'Power'!=w4.get() and 'Toughness'!=w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['CardType']==variable2.get() and CPT2[0]==w4.get() and CPT2[1]==w5.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done color, power and toughness')

        elif variable1.get() != 'Rarity' and variable2.get() !='Type' and mana[mana3] =='Color' and 'Power'==w4.get() and 'Toughness'==w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['Rarity'] == variable1.get() and d['CardType']==variable2.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done rarity and type')

        elif variable1.get() != 'Rarity' and variable2.get() =='Type' and mana[mana3] !='Color' and 'Power'==w4.get() and 'Toughness'==w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['Rarity'] == variable1.get() and mana[mana3] in d['Mana'] :
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done rarity and color')

        elif variable1.get() != 'Rarity' and variable2.get() =='Type' and mana[mana3] =='Color' and 'Power'!=w4.get() and 'Toughness'==w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['Rarity'] == variable1.get() and CPT2[0]==w4.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done rarity and power')

        elif variable1.get() != 'Rarity' and variable2.get() =='Type' and mana[mana3] =='Color' and 'Power'==w4.get() and 'Toughness'!=w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['Rarity'] == variable1.get() and CPT2[1]==w5.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done rarity and toughness')

        elif variable1.get() == 'Rarity' and variable2.get() !='Type' and mana[mana3] !='Color' and 'Power'==w4.get() and 'Toughness'==w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['CardType']==variable2.get() and mana[mana3] in d['Mana']:
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done type and color')

        elif variable1.get() == 'Rarity' and variable2.get() !='Type' and mana[mana3] =='Color' and 'Power'!=w4.get() and 'Toughness'==w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['CardType']==variable2.get() and CPT2[0]==w4.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done type and power')

        elif variable1.get() == 'Rarity' and variable2.get() !='Type' and mana[mana3] =='Color' and 'Power'==w4.get() and 'Toughness'!=w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['CardType']==variable2.get() and CPT2[1]==w5.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done type and toughness')

        elif variable1.get() == 'Rarity' and variable2.get() =='Type' and mana[mana3] !='Color' and 'Power'!=w4.get() and 'Toughness'==w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if mana[mana3] in d['Mana'] and CPT2[0]==w4.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done color and power')

        elif variable1.get() == 'Rarity' and variable2.get() =='Type' and mana[mana3] !='Color' and 'Power'==w4.get() and 'Toughness'!=w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if mana[mana3] in d['Mana'] and CPT2[1]==w5.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('color and toughness')

        elif variable1.get() == 'Rarity' and variable2.get() =='Type' and mana[mana3] =='Color' and 'Power'!=w4.get() and 'Toughness'!=w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if CPT2[0]==w4.get() and CPT2[1]==w5.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done power and toughness')

        elif variable1.get() != 'Rarity' and variable2.get() =='Type' and mana[mana3] =='Color' and 'Power'==w4.get() and 'Toughness'==w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['Rarity'] == variable1.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done rarity only')

        elif variable1.get() == 'Rarity' and variable2.get() !='Type' and mana[mana3] =='Color' and 'Power'==w4.get() and 'Toughness'==w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if d['CardType']==variable2.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done type only')

        elif variable1.get() == 'Rarity' and variable2.get() =='Type' and mana[mana3] !='Color' and 'Power'==w4.get() and 'Toughness'==w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if mana[mana3] in d['Mana']:
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done color only')

        elif variable1.get() == 'Rarity' and variable2.get() =='Type' and mana[mana3] =='Color' and 'Power'!=w4.get() and 'Toughness'==w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if CPT2[0]==w4.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done power only')

        elif variable1.get() == 'Rarity' and variable2.get() =='Type' and mana[mana3] =='Color' and 'Power'==w4.get() and 'Toughness'!=w5.get():
            for d in Cards.values():
                CPT=d['P/T']
                CPT2=CPT.split('/')
                if CPT2[1]==w5.get():
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
            print('done toughness only')

    button = Button(frame, text="Search", command=ok)
    button.grid(row = 6, column = 2, pady = 2)

    button2 = Button(frame, text="Reset", command=Reset)
    button2.grid(row = 6, column = 1, pady = 2)

def List():
    for widget in frame.winfo_children():
        widget.destroy()
    lbl = Label(frame, text = "Card Name:")
    lbl.grid(column =0, row =1)
    
    txt = Entry(frame, width=10)
    txt.grid(column =1, row =1)

    lbl2 = Label(frame, text = "File Name:")
    lbl2.grid(column =0, row =2)
    
    txt2 = Entry(frame, width=10)
    txt2.grid(column =1, row =2)

    def clicked1():
        card=txt.get()
        for d in cards.values():
            if d['CardName']==card:
                a=(f'{d["CardName"]}= {d["CardType"]}= {d["SubType"]}= {d["P/T"]}= {d["Mana"]}= {d["Rarity"]}')
                c=a.split('= ')
                name=c[0]
                name.strip('"')
                cardin={'CardName':c[0],'CardType': c[1], 'SubType': c[2], 'P/T': c[3], 'Mana' : c[4], 'Rarity':c[5]}
                allcards[name]=cardin
        txt.delete(0,END)
        txt2.delete(0,END)

    def clicked2():
        try:
            file=open(txt2.get()+'.py', "r")
            file2= ast.literal_eval(file.read())
            file.close()
            file3=merge(file2, allcards)
            file=open(txt2.get()+'.py', "w")
            file.write(str(file3))
            file.close
            print('1')
        except:
            f = open(txt2.get()+'.py', "w")
            f.write(str(allcards))
            f.close()
            print('2')
                
    btn = Button(frame, text = "Add Card" , command=clicked1)
    btn.grid(column=2, row=1)

    btn2 = Button(frame, text = "Done" , command=clicked2)
    btn2.grid(column=2, row=2)

men = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Options', menu = men) 
men.add_command(label ='List', command = List) 
men.add_command(label ='Filter', command = filter) 

master.config(menu = menubar)
mainloop()