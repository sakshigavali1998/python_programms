str = input("enter sentence:")
c1 = 0
c2 = 0

for i in str:
    if(i.isdigit()):
        c1 = c1+1

print(c1)

for j in str:
    if(j.isupper()):
        c2 = c2+1

print(c2)