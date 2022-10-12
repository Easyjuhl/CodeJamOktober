for i in range(int(input())):
    shift = int(input())
    string = input()
    string = string.split()
    output = ""
    for i in string:
        if shift >= 0:
            for j in range(shift):
                i = i[-1]+i
                i = i[:-1]
        else:
            for j in range(abs(shift)):
                i = i + i[0]
                i = i[1:]
        output += (i+" ")
    print(output[:-1])