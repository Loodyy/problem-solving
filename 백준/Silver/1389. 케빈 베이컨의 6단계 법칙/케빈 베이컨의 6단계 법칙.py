import sys
input = sys.stdin.readline

n, m = map(int, input().split())

INF = int(1e9)
conn = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            conn[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    conn[a][b] = 1
    conn[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            conn[i][j] = min(conn[i][j], conn[i][k]+conn[k][j])

minV, targ = INF, -1
for idx in range(1, n+1):
    if minV > sum(conn[idx][1:]):
        minV = sum(conn[idx][1:])
        targ = idx

print(targ)