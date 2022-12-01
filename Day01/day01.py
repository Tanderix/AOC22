def readfile(f):
    sums = []
    esum = 0
    for num in f:
        if num == "\n":
            sums.append(esum)
            esum = 0
        else:
            esum = esum + int(num)
    return sums


f = open("C:\\Users\\andre\\PycharmProjects\\AOC22\\d1input.txt", "r")
elist = readfile(f)
elist.sort(reverse=True)
print(elist[0])
print(elist[0]+elist[1]+elist[2])
f.close()
