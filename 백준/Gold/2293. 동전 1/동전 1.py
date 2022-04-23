def solve():

    dp = [0] * (k+1)
    dp[0] = 1
    for x in arr:
        for j in range(1, k+1):
            if j-x >= 0:
                dp[j] += dp[j-x]
    
    print(dp[k])
    return

if __name__ == "__main__":

    n, k = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    arr.sort()

    solve()
