with open("input.txt") as f:
    l = [int(x.strip()) for x in f]

for i, n1 in enumerate(l):
    for j, n2 in enumerate(l[i+1:]):
            if n1 + n2== 2020:
                print(n1 * n2)

