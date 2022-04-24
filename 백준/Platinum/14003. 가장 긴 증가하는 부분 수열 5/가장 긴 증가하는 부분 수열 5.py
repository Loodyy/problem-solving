def solve():

    dp = [arr[0]]
    dp_leng = [1] * n
    for i in range(1, n):
        if arr[i] > dp[-1]:
            dp.append(arr[i])
            dp_leng[i] = len(dp)
        else:
            idx = bisect(dp, arr[i])
            dp[idx] = arr[i]
            dp_leng[i] = idx + 1
    
    result = []
    idx = max(dp_leng)
    for i in range(n-1, -1, -1):
        if dp_leng[i] == idx:
            result.append(arr[i])
            idx -= 1
    result.reverse()

    print(len(result))
    for x in result:
        print(x, end=' ')
    return

def bisect(arr, x):

    l, r = 0, len(arr)-1
    idx = 0
    while l <= r:
        mid = (l+r)//2
        if arr[mid] >= x:
            r = mid - 1
            idx = mid
        else: l = mid + 1
    return idx

if __name__ == "__main__":

    n = int(input())
    arr = list(map(int, input().split()))

    solve()
