def find_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return i


def find_common3(list1, list2, list3):
    for i in list1:
        for j in list2:
            if i == j:
                for k in list3:
                    if i == j == k:
                        return k


def find_priority(char):
    if char.islower():
        return ord(char)-96
    else:
        return ord(char)-38


def part1(file):
    prioritysum = 0
    for sack in file:
        sack = sack.strip("\n")
        half = int((len(sack)) / 2)
        comp1 = sack[0:half]
        comp2 = sack[half:]
        common = find_common(comp1, comp2)
        common2 = set(comp1).intersection(comp2)
        prioritysum = prioritysum + find_priority(common)
    return prioritysum


def part2(file):
    prioritysum = 0
    for i in range(1, 101):
        sack1 = (file.readline())
        sack2 = (file.readline())
        sack3 = (file.readline())
        common3 = find_common3(sack1, sack2, sack3)
        prioritysum = prioritysum + find_priority(common3)
    return prioritysum


f1 = open("d3input.txt", "r")
f2 = open("d3input.txt", "r")
print(part1(f1))
print(part2(f2))

