a = input("enter 4 digit numbers")
lst = a.split(",")
print(lst)
b = []
for i in lst:
    b.append(int(i,2))
print(b)
for i in b:

    if (i%5 == 0):
        x = bin(i)
        print (x,end = ",")