def solve():

    a, b = len(x), len(y)
    dp = [[0] * (b+1) for _ in range(a+1)]
    for i in range(1, a+1):
        for j in range(1, b+1):
            if x[i-1] == y[j-1]: dp[i][j] = dp[i-1][j-1] + 1
            else: dp[i][j] = max(dp[i][j-1], dp[i-1][j]) 
    
    print(dp[a][b])
    return

if __name__ == "__main__":

    x = input()
    y = input()

    solve()
