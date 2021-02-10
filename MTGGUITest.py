from tkinter import *
from CardInfo import cards 

rarity1=['Rarity', 'Rare', 'Uncommon', 'Common', 'Mythic Rare', 'Bonus', 'Special', 'Promo']
types=['Type','Enchantment', 'Creature', 'Sorcery', 'Instant', 'Land', 'Artifact', 'Planeswalker', 'Artifact Creature', 'Enchantment Creature', 'Tribal Sorcery', 'Artifact Land', 'Enchantment Artifact', 'Tribal Enchantment', 'Tribal Instant', 'Tribal Artifact', 'Land Creature', 'Enchantment Land', 'Instant Creature']
mana=['Color','R','B','U','W','G']
mana2=['Color','Red','Black','Blue','White','Green']


master = Tk()
master.title('GUI Test')
master.geometry('450x300')

#Rarity Drop Down
variable1 = StringVar(master)
variable1.set(rarity1[0]) # default value
w1 = OptionMenu(master, variable1, *rarity1)
w1.grid(row = 0, column = 2, pady = 2)
l1 = Label(master, text = "Rarity:") 
l1.grid(row = 0, column = 1, pady = 2)

#Type Drop Down
variable2 = StringVar(master)
variable2.set(types[0]) # default value
w2 = OptionMenu(master, variable2, *types)
w2.grid(row = 1, column = 2, pady = 2)
l2 = Label(master, text = "Type:") 
l2.grid(row = 1, column = 1, pady = 2)

#Mana Drop Down
variable3 = StringVar(master)
variable3.set(mana[0]) # default value
w3 = OptionMenu(master, variable3, *mana2 )
w3.grid(row = 2, column = 2, pady = 2)
l5 = Label(master, text = "Mana:") 
l5.grid(row = 2, column = 1, pady = 2)

#Power text box
w4 = Entry(master, width=10)
w4.grid(row = 3, column = 2, pady = 2)
l4 = Label(master, text = "Power:") 
l4.grid(row = 3, column = 1, pady = 2)

#toughness text box
w5 = Entry(master, width=10)
w5.grid(row = 4, column = 2, pady = 2)
l5 = Label(master, text = "Toughness:") 
l5.grid(row = 4, column = 1, pady = 2)


listbox = Listbox(master, height = 15,  
                  width = 30,  
                  bg = "light grey", 
                  activestyle = 'dotbox',  
                  font = "Helvetica", 
                  fg = "black") 
listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 7, padx = 5, pady = 5)

def ok():
    print(w4.get(),w5.get())
    mana3=mana2.index(variable3.get())
    listbox.delete(0, listbox.size())
    if variable1.get() != 'Rarity' and variable2.get() !='Type' and mana[mana3] !='Color' and w4.get()!='' and w5.get()!='':
        for d in cards.values():
            if d['Rarity'] == variable1.get() and d['CardType']==variable2.get() and mana[mana3] in d['Mana']:
                listbox.insert(listbox.size(),d['CardName'])
        listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
        print('done rarity, type, color')

    elif variable1.get() != 'Rarity' and variable2.get() =='Type' and mana[mana3] !='Color':
        for d in cards.values():
            if d['Rarity'] == variable1.get() and mana[mana3] in d['Mana']:
                listbox.insert(listbox.size(),d['CardName'])
        listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
        print('done rarity and color')
    
    elif variable1.get() == 'Rarity' and variable2.get() !='Type' and mana[mana3] !='Color':
        for d in cards.values():
            if d['CardType']==variable2.get() and mana[mana3] in d['Mana']:
                listbox.insert(listbox.size(),d['CardName'])
        listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
        print('done type and color')
    
    elif variable1.get() != 'Rarity' and variable2.get() !='Type' and mana[mana3] =='Color':
        for d in cards.values():
            if d['Rarity'] == variable1.get() and d['CardType']==variable2.get():
                listbox.insert(listbox.size(),d['CardName'])
        listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
        print('done rarity and type')
    
    elif variable1.get() != 'Rarity' and variable2.get() =='Type' and mana[mana3] =='Color':
        for d in cards.values():
            if d['Rarity'] == variable1.get():
                listbox.insert(listbox.size(),d['CardName'])
        listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
        print('done rarity only')
    
    elif variable1.get() == 'Rarity' and variable2.get() !='Type'and mana[mana3] =='Color':
        for d in cards.values():
            if d['CardType']==variable2.get():
                listbox.insert(listbox.size(),d['CardName'])
        listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5)
        print('done type only')
    
    elif variable1.get() == 'Rarity' and variable2.get() =='Type' and mana[mana3] !='Color':
            for d in cards.values():
                if mana[mana3] in d['Mana']:
                    listbox.insert(listbox.size(),d['CardName'])
            listbox.grid(row = 0, column = 3, columnspan = 4, rowspan = 6, padx = 5, pady = 5) 
            print('done color only')

button = Button(master, text="Search", command=ok)
button.grid(row = 5, column = 2, pady = 2)

mainloop()