def solve(n):

    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        for j in [1, 2, 3]:
            if i-j >= 0:
                dp[i] += dp[i-j]

    return dp[n]

k = int(input())
for _ in range(k):
    print(solve(int(input())))