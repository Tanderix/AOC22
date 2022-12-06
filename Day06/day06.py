def marker(f, n):
    data = f.readline()
    slices = []
    for c in range(0, len(data) - n):
        slices.append(data[c:c + n])
    for (index, substring) in enumerate(slices):
        if len(set(substring)) == len(substring):
            return index + n


f1 = open("d6input.txt", "r")
f2 = open("d6input.txt", "r")
print(f"Part 1: {marker(f1, 4)}")
print(f"Part 2: {marker(f2, 14)}")
