str = input("enter sentence:")
count1 = 0
count2 = 0

for i in str:
    if(i.islower()):
        count1 = count1+1

print(count1)

for j in str:
    if(j.isupper()):
        count2 = count2+1

print(count2)