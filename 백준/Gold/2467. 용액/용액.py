n = int(input())
arr = list(map(int, input().split()))

min_abs = float('inf')
ans = None
for i in range(n):
    prev = arr[i]

    s, e = 0, n-1
    while s <= e:
        if s == i:
            s += 1
            continue
        if e == i:
            e -= 1
            continue
        mid = (s+e)//2
        curr = prev + arr[mid] 
        if abs(curr) < min_abs:
            min_abs = abs(curr)
            ans = (arr[i], arr[mid])
        
        if curr < 0:
            s = mid + 1
        else:
            e = mid - 1

print(*ans)