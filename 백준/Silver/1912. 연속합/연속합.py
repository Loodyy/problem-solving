def solve(n, arr):

    dp = [x for x in arr]
    for i in range(1, n):
        dp[i] = max(dp[i], dp[i-1]+arr[i])

    return max(dp)

def main():

    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n, arr))

if __name__ == "__main__":

    main()
    
