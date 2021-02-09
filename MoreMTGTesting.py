a=input()

f = open("test.txt", "r")
for x in f:
    b=(f.readline())
    b.split('. ')
    if a in b:
        print(b)