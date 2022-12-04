def toList(assignment):
    start, finish = assignment.split("-")
    return [x for x in range(int(start), int(finish)+1)]


f = open("d4input.txt", "r")
contained = 0
overlap = 0
for asspair in f:
    asspair = asspair.strip("\n")
    e1, e2 = asspair.split(",")
    l1 = (toList(e1))
    l2 = (toList(e2))

    # Part 2
    if set(l1) & set(l2) != set():
        overlap += 1

    # Part 1
    if set(l1) & set(l2) == set(l2) or set(l1) & set(l2) == set(l1):
        contained += 1

print("Part 1: " + str(contained))
print("Part 2: " + str(overlap))


