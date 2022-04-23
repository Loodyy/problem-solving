def bisect(arr, x):
    
    l, r, idx = 0, len(arr)-1, 0
    while l <= r:
        mid = (l+r)//2
        if arr[mid] >= x:
            r = mid - 1
            idx = mid
        else: l = mid + 1
    return idx

def solve():

    dp = [arr[0]] 
    for i in range(1, n):
        if arr[i] > dp[-1]:
            dp.append(arr[i])
        else:
            dp[bisect(dp, arr[i])] = arr[i]

    print(len(dp))    
    return

if __name__ == "__main__":

    n = int(input())
    arr = list(map(int, input().split()))
    
    solve()
