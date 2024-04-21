import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

sums = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        sums[i][j] = arr[i-1][j-1] + sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    res = sums[x2][y2] - sums[x2][y1-1] - sums[x1-1][y2] + sums[x1-1][y1-1]
    print(res)