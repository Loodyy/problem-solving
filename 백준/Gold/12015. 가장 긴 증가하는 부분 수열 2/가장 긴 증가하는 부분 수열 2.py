n = int(input())
arr = list(map(int, input().split()))

def bisect(arr, i):
    l = 0
    r = len(arr) - 1
    idx = 0
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] >= i:
            idx = mid
            r = mid - 1
        else:
            l = mid + 1
    return idx

dp = [arr[0]]
for i in range(1, n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        index = bisect(dp, arr[i])
        dp[index] = arr[i]

print(len(dp))

