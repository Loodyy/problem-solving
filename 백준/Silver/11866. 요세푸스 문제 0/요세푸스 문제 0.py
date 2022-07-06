n, k = map(int, input().split())
arr = list(range(1, n+1))
res, idx = [], 0
while arr:
    idx = (idx+k-1)%len(arr)
    res.append(str(arr.pop(idx)))

print("<"+", ".join(res)+">")