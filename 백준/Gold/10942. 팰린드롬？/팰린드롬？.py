import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
queries = [tuple(map(int, input().split())) for _ in range(M)]

dp = [[0] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1

for i in range(1, N):
    for j in range(N):
        if j+i >= N:
            break
        if arr[j] != arr[j+i]:
            continue
        if i == 1 or dp[j+1][j+i-1] == 1:
            dp[j][j+i] = 1
            dp[j+i][j] = 1

for query in queries:
    print(dp[query[0]-1][query[1]-1])