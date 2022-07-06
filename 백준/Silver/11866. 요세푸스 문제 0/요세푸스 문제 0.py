n, k = map(int, input().split())
arr = list(range(1, n+1))
idx, cnt, total = -1, 0, 0
res = []
while total < n:
    if arr[idx%n] == 0:
        idx += 1
        continue
    if cnt == k:
        res.append(str(arr[idx%n]))
        total += 1
        arr[idx%n], cnt = 0, 0
    idx += 1
    cnt += 1

print("<"+", ".join(res)+">")