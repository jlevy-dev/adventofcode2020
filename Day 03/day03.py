with open("input.txt") as f:
    lines = [x.strip() for x in f]
treesEncountered = 0
n1=0
n2=0

for y in lines:

    if lines [n1][n2 % 31] == '#':
        n1 += 1
        n2 += 3
        treesEncountered += 1
    else:
        n1 += 1
        n2 += 3


print(treesEncountered)
