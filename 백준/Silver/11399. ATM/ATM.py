n = int(input())
line = list(map(int, input().split()))
line.sort()

res, t = 0, 0
for l in line:
    t += l
    res += t

print(res)