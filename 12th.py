a=[]
a=str(input("enter sequence of no : "))
b=a.split(",")
print(b)
for i in range(0,len(b)):
    b[i]=int(b[i])

for i in b:
    if i%2!=0:
        s=i*i
        print(s,end=" ")