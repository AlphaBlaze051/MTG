import csv

allcards={}

with open('output.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        if 'token' not in row["cardName"]:
            a=(f'{row["cardName"]}= {row["cardType"]}= {row["subType"]}= {row["typeNum"]}= {row["manaCost"]}= {row["rarity"]}')
            c=a.split('= ')
            name=c[0]
            name.strip('"')
            cardin={'CardName':c[0],'CardType': c[1], 'SubType': c[2], 'P/T': c[3], 'Mana' : c[4], 'Rarity':c[5]}
            allcards[name]=cardin
            line_count += 1
f = open("test.txt", "a")
f.write(str(allcards))
f.close()