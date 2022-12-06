def movecrates(f, part):
    stacks = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: []
    }

    exitloop = False
    characters = 0
    # Create stacks of crates
    for line in f:
        if exitloop: break
        for c in line:
            characters += 1
            if c.isalpha():
                if characters == 2:
                    index = 1
                else:
                    index = int((int(characters) + 2) / 4)
                old = stacks.get(index)
                old.append(c)
                stacks.update({index: old})
            elif c == "\n":
                characters = 0
            elif c.isdecimal():
                exitloop = True

    for move in f:
        comlist = move.strip("\n").split(" ")
        com = [int(x) for x in comlist if x.isnumeric()]
        # com[0]: how many crates
        # com[1]: start
        # com[2]: destination
        oldcrate = stacks.get(com[1])
        newcrate = stacks.get(com[2])
        tomove = []
        for i in range(1, com[0] + 1):
            tomove.append(oldcrate.pop(0))
        if part == 2:
            tomove.reverse()
        for i in range(0, com[0]):
            newcrate.insert(0, tomove[i])

        stacks.update({com[1]: oldcrate})
        stacks.update({com[2]: newcrate})

    # Find top of each stack
    result = ""
    for i in range(1, 11):
        if stacks.get(i) is not None:
            result += stacks.get(i)[0]
    return result


f1 = open("d5input.txt", "r")
f2 = open("d5input.txt", "r")
Part1 = movecrates(f1, 1)
Part2 = movecrates(f2, 2)
print(f"Part 1: {Part1}")
print(f"Part 2: {Part2}")
