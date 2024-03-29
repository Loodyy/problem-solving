n = int(input())
arr = list(map(int, input().split()))
ans = [0] * n

num_map = dict()
for i, num in enumerate(arr):
    num_map[num] = i

max_num = max(arr)
for i, num in enumerate(arr):
    mul = 1
    cur = num
    while cur <= max_num:
        if cur in num_map and not num_map[cur] == i:
            ans[i] += 1
            ans[num_map[cur]] -= 1
        mul += 1
        cur = num * mul 

print(*ans)