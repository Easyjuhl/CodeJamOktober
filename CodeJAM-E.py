
current = input()
maplist = []
while current != "":
    list = []
    for i in current:
        list.append(i)
    maplist.append(list)
    current = input()
print(maplist)

dic = {}

for i in range(len(maplist)):
    for j in range(len(maplist[0])):
        if maplist[i][j] == "@":
            dic[(i, j)] = True
        else:
            dic[(i, j)] = False

change = True
while change:
    change = False
    for i in range(len(maplist)):
        print("still running")
        for j in range(len(maplist[0])):
            if maplist[i][j] == "." and not dic[(i, j)]:
                try:
                    if dic[(i-1, j)]:
                        dic[(i, j)] = True
                        change = True
                except KeyError:
                    pass

                try:
                    if dic[(i+1, j)]:
                        dic[(i, j)] = True
                        change = True
                except KeyError:
                    pass

                try:
                    if dic[(i, j-1)]:
                        dic[(i, j)] = True
                        change = True
                except KeyError:
                    pass

                try:
                    if dic[(i, j+1)]:
                        dic[(i, j)] = True
                        change = True
                except KeyError:
                    pass

output = 0
for i in range(len(maplist)):
    for j in range(len(maplist[0])):
        if dic[(i, j)]:
            output += 1

print(output)
#print(dic)