def slope(dx, dy):
    with open("input.txt") as f:
        lines = [x.strip() for x in f]
    x = 0
    y = 0
    treesEncountered = 0
    while y  < len(lines):
        if lines[y][x % 31] == '#':
            treesEncountered += 1
        x += dx
        y += dy

    return treesEncountered

print(slope(3,1))
print(slope(1,1)*slope(3,1)*slope(5,1)*slope(7,1)*slope(1,2))
