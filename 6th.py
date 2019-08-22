lines = []
while True:
    i = input()
    if i:
        lines.append(i.upper())
    else:
        break
for i in lines:
    print(i)