a = input("Enter sentance : ")
b=a.split(' ')
print(b)
c= set(b)
print(c)
print(' '.join(sorted(c)))