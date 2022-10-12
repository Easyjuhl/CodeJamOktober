for i in range(int(input())):
    shift = int(input())
    string = input()
    if shift >= 0:
        for i in range(shift):
            string = string[-1]+string
            string = string[:-1]
    else:
        for i in range(abs(shift)):
            string = string + string[0]
            string = string[1:]
    print(string)

