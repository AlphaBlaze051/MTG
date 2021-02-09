import csv

allcards=[]

with open('output.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        a=(f'{row["cardName"]}. {row["cardType"]}-{row["subType"]}. {row["typeNum"]}. {row["manaCost"]}. {row["rarity"]}')
        if row['subType']=='':
            a=(f'{row["cardName"]}. {row["cardType"]}. {row["typeNum"]}. {row["manaCost"]}. {row["rarity"]}')
            if row["typeNum"]=='':
                a=(f'{row["cardName"]}. {row["cardType"]}. {row["manaCost"]}. {row["rarity"]}')
        else:
            if row["typeNum"]=='':
                a=(f'{row["cardName"]}. {row["cardType"]}-{row["subType"]}. {row["manaCost"]}. {row["rarity"]}')
        allcards.append(a)
        line_count += 1
    mylist = list(dict.fromkeys(allcards))
for i in range(len(mylist)):
    f = open("test.txt", "a")
    f.write(mylist[i]+'\n')
    f.close()
