def solve():

    result = []

    dp = [1 for _ in range(n)]
    rdp = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
            if rearr[j] < rearr[i]:
                rdp[i] = max(rdp[i], rdp[j]+1)
    for i in range(n):
        result.append(dp[i] + rdp[n-i-1] - 1)

    print(max(result))
    return

if __name__ == "__main__":

    n = int(input())
    arr = list(map(int, input().split()))
    rearr = arr[::-1]

    solve()
