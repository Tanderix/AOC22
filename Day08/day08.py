f1 = open("day08input.txt", "r")
maxlen = 0
for line in f1:
    newline = line.strip("\n")
    if len(newline) > maxlen:
        maxlen = len(newline)
f1.close()

f1 = open("day08input.txt", "r")
forest = [
]
# Create forest
for line in f1:
    forest.append([*line.strip("\n")])

# Print forest
# for treerow in forest:
    # print(treerow)

# Check trees
visible = 0
visibles = []
visibilityleft = 0
visibilityright = 0
visibilitytop = 0
visibilitybottom = 0

for x in range(maxlen):
    for y in range(len(forest)):
        # Check elements
        # If is edge
        current = forest[x][y]
        if (x - 1) < 0 or (y - 1) < 0 or (x + 1) == maxlen or (y + 1) == len(forest):
            if (x, y) not in visibles:
                visibles.append((x, y))
            visible += 1
        else:
            # Check top
            visiblefromtop = True
            if (x, y) not in visibles:
                for i in range(x-1, -1, -1):
                    tocheck = forest[i][y]
                    if tocheck >= current:
                        visiblefromtop = False

                if visiblefromtop:
                    visibles.append((x, y))
                    visible += 1

            # Check bottom
            visiblefrombottom = True
            if (x, y) not in visibles:
                for j in range(x+1, len(forest)):
                    tocheck = forest[j][y]
                    if tocheck >= current:
                        visiblefrombottom = False

                if visiblefrombottom:
                    visibles.append((x, y))
                    visible += 1

            # Check right
            visiblefromright = True
            if (x, y) not in visibles:
                for i in range(y+1, maxlen):
                    tocheck = forest[x][i]
                    if tocheck >= current:
                        visiblefromright = False

                if visiblefromright:
                    visibles.append((x, y))
                    visible += 1

            # Check right
            visiblefromleft = True
            if (x, y) not in visibles:
                for i in range(y-1, -1, -1):
                    tocheck = forest[x][i]
                    if tocheck >= current:
                        visiblefromleft = False

                if visiblefromleft:
                    visibles.append((x, y))
                    visible += 1

print(f"Part 1: {visible}")

scores = []
for x in range(maxlen):
    for y in range(len(forest)):

        # Top visibility
        current = forest[x][y]
        for i in range(x-1, -1, -1):
            tocheck = forest[i][y]
            if tocheck < current:
                visibilitytop += 1
            else:
                visibilitytop += 1
                break

        # Bottom visibility
        for j in range(x + 1, len(forest)):
            tocheck = forest[j][y]
            if tocheck < current:
                visibilitybottom += 1
            else:
                visibilitybottom += 1
                break

        # Right visibility
        for i in range(y + 1, maxlen):
            tocheck = forest[x][i]
            if tocheck < current:
                visibilityright += 1
            else:
                visibilityright += 1
                break

        # Left visibility
        for i in range(y - 1, -1, -1):
            tocheck = forest[x][i]
            if tocheck < current:
                visibilityleft += 1
            else:
                visibilityleft += 1
                break

        # Get scenic score per tree
        scenic_score = visibilitytop * visibilitybottom * visibilityleft * visibilityright
        scores.append(scenic_score)

        visibilityleft = 0
        visibilityright = 0
        visibilitytop = 0
        visibilitybottom = 0

print(f"Part 2: {max(scores)}")