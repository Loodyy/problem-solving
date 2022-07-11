import sys
input = sys.stdin.readline

n, tar = map(int, input().split())
coins = [int(input()) for _ in range(n)]

for i in range(n):
    if coins[i] > tar:
        idx = i-1
        break
    idx = i

cnt = 0
for j in range(idx, -1, -1):
    cnt += tar//coins[j]
    tar %= coins[j]

print(cnt)