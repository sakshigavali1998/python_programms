from operator import itemgetter, attrgetter
data= []
while True:
    a= input()
    if not a:
        break
    data.append(tuple(a.split(",")))
print(sorted(data, key=itemgetter(0,1,2)))