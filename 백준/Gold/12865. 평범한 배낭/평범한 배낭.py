def solve():
    
    dp = [0] * (k+1)

    for i in range(n):
        for j in range(k, -1, -1):
            if j-arr[i][0] >= 0:
                dp[j] = max(dp[j], dp[j-arr[i][0]] + arr[i][1])

    print(dp[k])
    return

if __name__ == "__main__":

    n, k = map(int, input().split())
    arr = []
    for _ in range(n): 
        arr.append(list(map(int, input().split()))) # w, v
    
    solve()