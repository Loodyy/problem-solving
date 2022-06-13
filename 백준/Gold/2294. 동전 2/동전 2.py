def solve(n, k, arr):

    dp = [1e9] * (k+1)
    dp[0] = 0

    for i in range(1, k+1):
        for coin in arr:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i-coin]+1)

    if dp[k] == 1e9:
        dp[k] = -1
    return dp[k]

def main():

    n, k = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    print(solve(n, k, arr))

if __name__ == "__main__":

    main()
