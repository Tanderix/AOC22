# For better readability in the rest of the code
# A - rock, B - paper, C - scissors
# X - rock, Y - paper, Z - scissors
def getMoves(elf, me):
    match elf:
        case 'A':
            elf = "ROCK"
        case 'B':
            elf = "PAPER"
        case 'C':
            elf = "SCISSORS"

    match me:
        case 'X':
            me = "ROCK"
        case 'Y':
            me = "PAPER"
        case 'Z':
            me = "SCISSORS"
    return elf, me


# Get the losing move
def lose(played):
    match played:
        case "ROCK":
            return "SCISSORS"
        case "PAPER":
            return "ROCK"
        case "SCISSORS":
            return "PAPER"


# Gets the winning move
def win(played):
    match played:
        case "ROCK":
            return "PAPER"
        case "PAPER":
            return "SCISSORS"
        case "SCISSORS":
            return "ROCK"

# (Part 2) Chooses the right move based on if you have to win lose or draw
def part2(elf, me):
    match me:
        case "ROCK":
            me = lose(elf)
        case "PAPER":
            me = elf
        case "SCISSORS":
            me = win(elf)
    return me


f = open("d2input.txt", "r")
matchscore = 0
for game in f:
    elf, me = game.split(" ")
    me = me.strip("\n\n")
    elf, me = getMoves(elf, me)
    gamescore = 0
    me = part2(elf, me)
    match me:
        case "ROCK":
            gamescore += 1
        case "PAPER":
            gamescore += 2
        case "SCISSORS":
            gamescore += 3
    match (elf, me):
        case ("ROCK", "PAPER"):
            gamescore += 6
        case ("PAPER", "SCISSORS"):
            gamescore += 6
        case ("SCISSORS", "ROCK"):
            gamescore += 6
        case _:
            if elf == me:
                gamescore += 3
    matchscore += gamescore

print(matchscore)

