import json

f1 = open("day07input.txt", "r")
basetree = {
        "/": []
        }

working = []
for line in f1:
    command = line.strip("\n").split(" ")
    if command[1] == "cd":
        if command[2] == "..":
            working.pop()
        else:
            working.append(command[2])
    elif command[1] != "ls":
        if command[0].isnumeric():
            if working == ["/"]:
                update = basetree.get(working[0])
                update.append(command[0])
            else:
                path = tuple(working)
                update = basetree.get(path)
                update.append(command[0])
        if command[0] == "dir":
            if working == ["/"]:
                update = basetree.get(working[0])
                path = (working[0])
            else:
                path = ()
                for i in range(len(working)):
                    path = tuple(working)
                    update = basetree.get(path)
            newpath = working
            if len(newpath) == 1:
                newpath = (working[0], command[1])
            elif len(newpath) == 2:
                newpath = (working[0], working[1], command[1])
            elif len(newpath) == 3:
                newpath = (working[0], working[1], working[2], command[1])
            elif len(newpath) == 4:
                newpath = (working[0], working[1], working[2], working[3], command[1])
            elif len(newpath) == 5:
                newpath = (working[0], working[1], working[2], working[3], working[4], command[1])
            elif len(newpath) == 6:
                newpath = (working[0], working[1], working[2], working[3], working[4], working[5], command[1])
            elif len(newpath) == 7:
                newpath = (working[0], working[1], working[2], working[3], working[4], working[5], working[6], command[1])
            elif len(newpath) == 8:
                newpath = (working[0], working[1], working[2], working[3], working[4], working[5], working[6], working[7], command[1])
            elif len(newpath) == 9:
                newpath = (working[0], working[1], working[2], working[3], working[4], working[5], working[6], working[7], working[8], command[1])
            elif len(newpath) == 10:
                newpath = (working[0], working[1], working[2], working[3], working[4], working[5], working[6], working[7], working[8], working[9], command[1])
            elif len(newpath) == 11:
                newpath = (working[0], working[1], working[2], working[3], working[4], working[5], working[6], working[7], working[8], working[9], working[10], command[1])
            elif len(newpath) == 12:
                newpath = (working[0], working[1], working[2], working[3], working[4], working[5], working[6], working[7], working[8], working[9], working[10], working[11], command[1])

            update.append(newpath)
            basetree.update({newpath: []})

part1 = 0
def dircount(tree):
    totalsum = []
    for dir in tree:
        dirsum = 0
        dircontent = basetree.get(dir)
        if dircontent is not None:
            for i in range(len(dircontent)):
                content = dircontent[i]
                if str(content).isnumeric():
                    dirsum += int(content)
                else:
                    dirsum += int(dircount(basetree.get(content))[1])
        else:
            dirsum += int(dir)
        totalsum.append(dirsum)
    return [totalsum, sum(totalsum)]


dirsizes = dircount(basetree)[0]

# Part 1
Part1 = 0
less = []
for i in dirsizes:
    if i <= 100000:
        less.append(i)
        Part1 += i

# Part 2
Part2 = 0
dirsizes.sort()
freenow = 70_000_000 - dirsizes[len(dirsizes)-1]
freeneeded = 30_000_000 - freenow

for size in dirsizes:
    if size >= freeneeded:
        Part2 = size
        break

print(f"Part 1: {Part1}")
print(f"Part 2: {Part2}")
