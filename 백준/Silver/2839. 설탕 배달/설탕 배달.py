def solve(n):
    result = 0

    dp = [1e9] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        for bag in [3, 5]:
            if i-bag >= 0:
                dp[i] = min(dp[i], dp[i-bag]+1)

    result = dp[n] if dp[n] != 1e9 else -1
    return result

def main():

    n = int(input())
    print(solve(n))

if __name__ == "__main__":

    main()
