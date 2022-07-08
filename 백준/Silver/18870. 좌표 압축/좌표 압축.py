n = int(input())
xpos = list(map(int, input().split()))

xs = sorted(list(set(xpos)))
x_idx = {x: i for i, x in enumerate(xs)}

for i in range(n):
    xpos[i] = x_idx[xpos[i]]

print(*xpos)