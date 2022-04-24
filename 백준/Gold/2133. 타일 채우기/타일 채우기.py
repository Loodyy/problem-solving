def solve():

    dp = [0] * (n+1)
    if n > 1: dp[2] = 3
    for i in range(3, n+1):
        if not i%2:
            dp[i] = dp[i-2] * 3 + sum(dp[:i-2])*2 + 2 

    print(dp[n])
    return

if __name__ == "__main__":

    n = int(input())

    solve()
