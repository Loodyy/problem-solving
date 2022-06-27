def solve(n, arr):
    arr.sort()
    presum = [0] * (n+1)
    for i in range(n):
        presum[i+1] = presum[i]+arr[i] 

    answer = n+1
    minV = 1e11
    for idx in range(n):
        pivot = arr[idx]
        cost = idx*pivot-presum[idx] + presum[n]-presum[idx+1]-(n-1-idx)*pivot
        if cost == minV:
            answer = min(answer, pivot)
        elif cost < minV:
            minV = cost
            answer = pivot
    return answer

n = int(input())
arr = list(map(int, input().split()))
print(solve(n, arr))