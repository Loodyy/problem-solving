def solve():

    dp = [1] * n
    temp = [[] for _ in range(n)]
    for i in range(n):
        temp[i].append(arr[i])
        tmp = []
        for j in range(i):
            if arr[i] > arr[j]:
                if dp[i] < dp[j]+1:
                    dp[i] = dp[j] + 1
                    tmp = temp[j]
        temp[i] += tmp
    temp.sort(key=lambda x: len(x))
    temp[n-1].reverse()
    print(len(temp[n-1]))
    for x in temp[n-1]:
        print(x, end=' ')
    return

if __name__ == "__main__":

    n = int(input())
    arr = list(map(int, input().split()))

    solve()
