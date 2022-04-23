from bisect import bisect_left

def solve():

    dp = [arr[0]] 
    for i in range(1, n):
        if arr[i] > dp[-1]:
            dp.append(arr[i])
        else:
            dp[bisect_left(dp, arr[i])] = arr[i]

    print(len(dp))    
    return

if __name__ == "__main__":

    n = int(input())
    arr = list(map(int, input().split()))

    solve()
