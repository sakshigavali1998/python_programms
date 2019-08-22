lst =[]
for i in range(1000,3001):
    a= str(i)
    if (int(a[0])%2==0) and (int(a[1])%2==0) and (int(a[2])%2==0) and (int(a[3])%2==0):
        lst.append(a)
print(','.join(lst))


