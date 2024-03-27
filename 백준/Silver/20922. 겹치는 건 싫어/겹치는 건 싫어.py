N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt_map = { A[0]: 1 }
ans = 1

s, e = 0, 1
while s <= e and e < N:
    if cnt_map.setdefault(A[e], 0) + 1 <= K:
        cnt_map[A[e]] += 1
        e += 1
        ans = max(ans, e - s)
    else:
        cnt_map[A[s]] -= 1
        s += 1

print(ans)