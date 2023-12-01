def printGrid(grid):
    for i in range(cols):
        for j in range(rows):
            if grid[i][j] in [['T'], ['H'], ['S'], ['T', 'H'], ['H', 'T']]:
                print(grid[i][j][0], end=" ")
            else:
                print(".", end=" ")
        print()
    print("-------------------------")


# [H]    |    [H] | [T]    |    [T]
#    [T] | [T]    |    [H] | [H]
def isdiagonal(HeadX, HeadY, TailX, TailY):
    if HeadX == TailX - 1 and HeadY == TailY - 1:
        return 1
    elif HeadX == TailX - 1 and HeadY == TailY + 1:
        return 2
    elif HeadX == TailX + 1 and HeadY == TailY + 1:
        return 3
    elif HeadX == TailX + 1 and HeadY == TailY - 1:
        return 4
    else:
        return -1


f1 = open("day09input.txt", "r")
# Crea griglia
rows, cols = (1000, 1000)
grid = [[[] for i in range(cols)] for j in range(rows)]


startposition = [500, 500]
ele = grid[startposition[0]][startposition[1]]
ele.append("S")
ele.append("H")
ele.append("T")
head = startposition
tail = startposition

currentposition = startposition
HeadX = currentposition[0]
HeadY = currentposition[1]

TailX = currentposition[0]
TailY = currentposition[1]


visited = []
for command in f1:
    direction, steps = command.strip("\n").split(" ")
    for i in range(0, int(steps)):
        grid[HeadX][HeadY].remove("H")
        grid[TailX][TailY].remove("T")
        if direction == "R":
            # Update tail
            if HeadY != TailY:
                if HeadY + 1 != TailY:
                    # If diagonal
                    diagonal = isdiagonal(HeadX, HeadY, TailX, TailY)
                    if diagonal != -1:
                        if diagonal == 2:
                            TailX -= 1
                            TailY += 1
                        elif diagonal == 3:
                            TailX += 1
                            TailY += 1
                    else:
                        if HeadY + 1 < cols:
                            TailY += 1
            # Update Head
            if HeadY + 1 < cols:
                HeadY += 1

        if direction == "U":
            # Update Tail
            if HeadX != TailX:
                if HeadX - 1 != TailX:
                    # If diagonal
                    diagonal = isdiagonal(HeadX, HeadY, TailX, TailY)
                    if diagonal != -1:
                        if diagonal == 1:
                            TailX -= 1
                            TailY -= 1
                        elif diagonal == 2:
                            TailX -= 1
                            TailY += 1
                    else:
                        if HeadX - 1 >= 0:
                            TailX -= 1
            # Update Head
            if HeadX - 1 >= 0:
                HeadX -= 1
        if direction == "L":
            # Update Tail
            if HeadY != TailY:
                if HeadY -1 != TailY:
                    diagonal = isdiagonal(HeadX, HeadY, TailX, TailY)
                    if diagonal != -1:
                        if diagonal == 1:
                            TailX -= 1
                            TailY -= 1
                        elif diagonal == 4:
                            TailX += 1
                            TailY -= 1
                    else:
                        if HeadY - 1 >= 0:
                            TailY -= 1

            # Update Head
            if HeadY - 1 >= 0:
                HeadY -= 1
        if direction == "D":
            if HeadX != TailX:
                if HeadX + 1 != TailX:
                    diagonal = isdiagonal(HeadX, HeadY, TailX, TailY)
                    if diagonal != -1:
                        if diagonal == 3:
                            TailX += 1
                            TailY += 1
                        elif diagonal == 4:
                            TailX += 1
                            TailY -= 1
                    else:
                        if HeadX + 1 < rows:
                            TailX += 1
            # Update head
            if HeadX + 1 < rows:
                HeadX += 1
        if [TailX, TailY] not in visited:
            visited.append([TailX, TailY])

        grid[HeadX][HeadY].append("H")
        grid[TailX][TailY].append("T")
print(f"Part 1: {len(visited)}")
"""
# --- Part 2 ---
f2 = open("day09input.txt", "r")
# Crea griglia
rows2, cols2 = (100, 100)
grid2 = [[[] for i in range(cols2)] for j in range(rows2)]
visited2 = []

startposition = [50, 50]
ele = grid2[startposition[0]][startposition[1]]
knots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
knotpositions = [[], [], [], [], [], [], [], [], [], []]
for i in range(len(knots)):
    knotpositions[i] = [startposition[0], startposition[1]]
    grid2[startposition[0]][startposition[1]].append(knots[i])


for command in f2:
    direction, steps = command.strip("\n").split(" ")
    for i in range(0, int(steps)):
        for j in range(0, len(knots)):
            current1 = knotpositions[j]
            current2 = knotpositions[j+1]
            HeadX = current1[0]
            HeadY = current1[1]

            TailX = current2[0]
            TailY = current2[1]
            print(knots[j])
            print(knots[j+1])
            grid2[HeadX][HeadY].remove(knots[j])
            grid2[TailX][TailY].remove(knots[j+1])
            if direction == "R":
                # Update tail
                if HeadY != TailY:
                    if HeadY + 1 != TailY:
                        # If diagonal
                        diagonal = isdiagonal(HeadX, HeadY, TailX, TailY)
                        if diagonal != -1:
                            if diagonal == 2:
                                TailX -= 1
                                TailY += 1
                            elif diagonal == 3:
                                TailX += 1
                                TailY += 1
                        else:
                            if HeadY + 1 < cols2:
                                TailY += 1
                # Update Head
                if HeadY + 1 < cols2:
                    HeadY += 1

            if direction == "U":
                # Update Tail
                if HeadX != TailX:
                    if HeadX - 1 != TailX:
                        # If diagonal
                        diagonal = isdiagonal(HeadX, HeadY, TailX, TailY)
                        if diagonal != -1:
                            if diagonal == 1:
                                TailX -= 1
                                TailY -= 1
                            elif diagonal == 2:
                                TailX -= 1
                                TailY += 1
                        else:
                            if HeadX - 1 >= 0:
                                TailX -= 1
                # Update Head
                if HeadX - 1 >= 0:
                    HeadX -= 1
            if direction == "L":
                # Update Tail
                if HeadY != TailY:
                    if HeadY - 1 != TailY:
                        diagonal = isdiagonal(HeadX, HeadY, TailX, TailY)
                        if diagonal != -1:
                            if diagonal == 1:
                                TailX -= 1
                                TailY -= 1
                            elif diagonal == 4:
                                TailX += 1
                                TailY -= 1
                        else:
                            if HeadY - 1 >= 0:
                                TailY -= 1

                # Update Head
                if HeadY - 1 >= 0:
                    HeadY -= 1
            if direction == "D":
                if HeadX != TailX:
                    if HeadX + 1 != TailX:
                        diagonal = isdiagonal(HeadX, HeadY, TailX, TailY)
                        if diagonal != -1:
                            if diagonal == 3:
                                TailX += 1
                                TailY += 1
                            elif diagonal == 4:
                                TailX += 1
                                TailY -= 1
                        else:
                            if HeadX + 1 < rows2:
                                TailX += 1
                # Update head
                if HeadX + 1 < rows2:
                    HeadX += 1
            if [TailX, TailY] not in visited2:
                visited2.append([TailX, TailY])

            grid2[HeadX][HeadY].append("H")
            grid2[TailX][TailY].append("T")
    printGrid(grid2)
"""