f1 = open("day11input.txt", "r")

monkeys = {

}

mn = 8
rounds = 10000

inspections = [0] * mn

modulo = 1

# Read input
def readmonkey(f1):
    monkeynumber = f1.readline().strip(":\n").split(" ")[1]
    startingitems = [x for x in f1.readline().replace(",", " ").replace("\n", " ").split(" ") if x.isnumeric()]
    operation = f1.readline().split(" ")
    operator = operation[6]
    operand = operation[7].strip("\n")
    test = f1.readline().split(" ")[5].strip("\n")
    iftrue = f1.readline().split(" ")[9].strip("\n")
    iffalse = f1.readline().split(" ")[9].strip("\n")
    f1.readline()
    return [monkeynumber, startingitems, operator, operand, test, iftrue, iffalse]


# Build starting monkeys
for i in range(0, mn):
    currentmonkey = readmonkey(f1)
    monkeys.update({currentmonkey[0]: currentmonkey})
    modulo *= int(currentmonkey[4])
currentmonkey = monkeys.get('0')


part = 2
if part == 1:
    rounds = 20

for j in range(1, rounds+1):
    for m in monkeys:
        currentmonkey = monkeys.get(m)
        # print(f"Monkey: {currentmonkey[0]}")
        itemlist = currentmonkey[1]
        for items in itemlist:
            # Update inspections
            inspections[int(currentmonkey[0])] += 1

            currentworry = int(items)
            # print(f"  Monkey inspects an item with a worry level of {items}")
            # Operation
            if currentmonkey[2] == '+':
                if currentmonkey[3].isnumeric():
                    currentworry += int(currentmonkey[3])
                else:
                    currentworry += currentworry
                # print(f"    Worry level increases by {currentmonkey[3]} to {currentworry}")
            elif currentmonkey[2] == '*':
                if currentmonkey[3].isnumeric():
                    currentworry *= int(currentmonkey[3])
                else:
                    currentworry *= currentworry
                # print(f"    Worry level is multiplied by {currentmonkey[3]} to {currentworry}")

            #Divide by 3:
            if part == 1:
                currentworry = currentworry // 3
            else:
                currentworry = currentworry % modulo
            # print(f"    Monkey gets bored with item. Worry level is divided by 3 to {currentworry}")

            # Test
            if currentworry % int(currentmonkey[4]) == 0:
                # If true
                # print(f"    Current worry level is divisible by {currentmonkey[4]}")
                target = currentmonkey[5]
            else:
                # If false
                # print(f"    Current worry level is not divisible by {currentmonkey[4]}")
                target = currentmonkey[6]


            #Update target
            aux = monkeys.get(target)
            # print(f"{target} + {aux}")
            aux[1].append(str(currentworry))
            monkeys.update({target: aux})
            # print(f"    Item with worry level {currentworry} is thrown to monkey {target}")

        # Update current
        aux = monkeys.get(currentmonkey[0])
        aux[1] = []
        monkeys.update({currentmonkey[0]: aux})
    # print(f"After round: {j}")

inspections.sort(reverse=True)
print(inspections[0] * inspections[1])