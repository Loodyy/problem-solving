n, k = map(int, input().split())
dp = [[0] * (n+1) for _ in range(k+1)]

for i in range(n+1):
    dp[1][i] = 1

for i in range(2, k+1):
    for j in range(n+1):
        for l in range(j+1):
            dp[i][j] += dp[i-1][j-l]

print(dp[k][n] % 1000000000)