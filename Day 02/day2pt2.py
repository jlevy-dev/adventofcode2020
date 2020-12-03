from collections import Counter

with open("input.txt") as f:
    lines = [x.strip() for x in f]

part1 = 0
part2 = 0

for l in lines:
    text = l.split()
    limits = text[0].split("-")
    lb, ub = int(limits[0]), int(limits[1])
    t = text[1][0]
    pw = text[2]

    counts = Counter(pw)[t]
    if lb <= counts <= ub:
        part1 += 1
    t_place1, t_place2 = pw[lb-1], pw[ub-1]
    if (t == t_place1) ^ (t == t_place2):
            part2 += 1
    
print(part1)
print(part2)
