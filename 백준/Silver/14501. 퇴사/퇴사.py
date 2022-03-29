import sys
input = sys.stdin.readline

def solve():  
    for i in range(n-1, -1, -1):
        x = arr[i]
        if i + x[0] <= n:
            dp[i] = max(dp[i+x[0]]+x[1] , dp[i+1])
        else:
            dp[i] = dp[i + 1]
    return max(dp)

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [0] * (n+1) 

    print(solve())