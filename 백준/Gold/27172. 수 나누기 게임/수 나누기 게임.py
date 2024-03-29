n = int(input())
arr = list(map(int, input().split()))
ans = [0] * n

num_set = dict()
max_num = max(arr)
for i in range(n):
    cur = arr[i]
    mul = 1
    while cur <= max_num:
        num_set.setdefault(cur, []).append(i)
        mul += 1
        cur = arr[i] * mul
        
for i in range(n):
    cur = arr[i]
    if cur in num_set:
        for j in num_set[cur]:
            if i == j:
                continue
            ans[i] -= 1
            ans[j] += 1

print(*ans)