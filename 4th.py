c = 50
h = 30
d = str(input("enter numbers:"))
lst = d.split(",")


for i in lst:
    q = ((2*c*int(i))/h) ** 0.5
    print (int(q),end=",")