def solve():

    dp = [0] * (n+1)

    for i in range(k):
        imp, t = arr[i][0], arr[i][1]
        for j in range(n, -1, -1):
            if j-t >= 0:
                dp[j] = max(dp[j], dp[j-t]+imp)
                
    print(max(dp))
    return

if __name__ == "__main__":

    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(k)]

    solve()
  
