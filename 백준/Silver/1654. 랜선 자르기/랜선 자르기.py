k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

l, r = 1, max(arr)
maxV = 0
while l <= r:
    mid = (l+r)//2
    cnt = 0
    for elem in arr:
        cnt += elem//mid

    if cnt >= n:
        maxV = max(maxV, mid)
        l = mid+1
    else:
        r = mid-1

print(maxV)