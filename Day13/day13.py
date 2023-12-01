import ast
import functools


def listorder(ele1, ele2):
    # Both numbers
    if isinstance(ele1, int) and isinstance(ele2, int):
        res = ele1 - ele2
        return res

    # Only first element is number
    if isinstance(ele1, int):
        return listorder([ele1], ele2)

    # Only second element is number
    elif isinstance(ele2, int):
        return listorder(ele1, [ele2])

    # Both lists
    for a, b in zip(ele1, ele2):
        result = listorder(a, b)
        if result != 0:
            return result

    return len(ele1) - len(ele2)


# Part 1
f1 = open("day13input.txt", "r")
pairs = []
lines = []
for i in range(0, 150):
    l1 = ast.literal_eval(f1.readline())
    l2 = ast.literal_eval(f1.readline())
    res = listorder(l1, l2)
    lines.append(l1)
    lines.append(l2)
    if res < 0:
        pairs.append(i+1)

    # Read blank line
    f1.readline()

print(f"Part1: {sum(pairs)}")
f1.close()

# Part 2
f1 = open("day13input.txt", "r")
pairs = []
lines = []
for i in range(0, 150):
    l1 = ast.literal_eval(f1.readline())
    l2 = ast.literal_eval(f1.readline())
    res = listorder(l1, l2)
    lines.append(l1)
    lines.append(l2)
    if res < 0:
        pairs.append(i+1)

    # Read blank line
    f1.readline()
lines.append([[2]])
lines.append([[6]])
lines = sorted(lines, key=functools.cmp_to_key(listorder))

key1 = lines.index([[2]])+1
key2 = lines.index([[6]])+1

print(f"Part2: {key1 * key2}")