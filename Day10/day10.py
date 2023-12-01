f1 = open("day10input.txt", "r")

# Part 1
totloops = 0
register = 1
checks = [20, 60, 100, 140, 180, 220]
signalstrengths = []

# Part 2
pixwidth = 40
pixheight = 6

spriterow = ["." for i in range(0, 40)]

spritepos = register
spriterow[spritepos] = "#"
spriterow[spritepos-1] = "#"
spriterow[spritepos+1] = "#"
beingdrawn = 0
currentrow = 0

crt = [[[] for i in range(pixwidth)] for j in range(pixheight)]
for command in f1:
    # instruction[0] = noop | addx
    # instruction[1] = n if istruction[0] is addx
    instruction = command.strip("\n").split(" ")
    if instruction[0] == "noop":
        # Draw in CRT
        if beingdrawn > pixwidth-1:
            beingdrawn = 0
            currentrow += 1

        tofind = [i for i, val in enumerate(spriterow) if val == '#']
        if beingdrawn in tofind:
            crt[currentrow][beingdrawn] = "#"
        else:
            crt[currentrow][beingdrawn] = "."

        # Update pixel to draw
        beingdrawn += 1

        totloops += 1
        if totloops in checks:
            signalstrengths.append(totloops * register)
            # print(f"Loop: {totloops} - Register: {register}")
    elif instruction[0] == "addx":
        # Cycle 1
        # Draw in CRT
        if beingdrawn > pixwidth-1:
            beingdrawn = 0
            currentrow += 1
        tofind = [i for i, val in enumerate(spriterow) if val == '#']
        if beingdrawn in tofind:
            crt[currentrow][beingdrawn] = "#"
        else:
            crt[currentrow][beingdrawn] = "."

        # Update pixel to draw
        beingdrawn += 1

        # Update loop count
        totloops += 1

        # Part 1 check
        if totloops in checks:
            signalstrengths.append(totloops * register)
            # print(f"Loop: {totloops} - Register: {register}")

        # Cycle 2
        # Draw in CRT
        if beingdrawn > pixwidth-1:
            beingdrawn = 0
            currentrow += 1

        tofind = [i for i, val in enumerate(spriterow) if val == '#']
        if beingdrawn in tofind:
            crt[currentrow][beingdrawn] = "#"
        else:
            crt[currentrow][beingdrawn] = "."

        # Update pixel to draw
        beingdrawn += 1

        # Update loop count
        totloops += 1

        # Part 1 check
        if totloops in checks:
            signalstrengths.append(totloops * register)
            # print(f"Loop: {totloops} - Register: {register}")

        # Update sprite position
        register += int(instruction[1])
        spriterow[spritepos] = "."
        spriterow[spritepos - 1] = "."
        spriterow[spritepos + 1] = "."
        spritepos = register
        spriterow[spritepos] = "#"
        spriterow[spritepos - 1] = "#"
        spriterow[spritepos + 1] = "#"
    else:
        print("Input error")

print(f"Part 1: {sum(signalstrengths)}")

print("Part 2: ")
for i in range(0, pixheight):
    for j in range(0, pixwidth):
        print(crt[i][j], end=" ")
    print()