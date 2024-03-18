import sys
input = sys.stdin.readline

n, h = map(int, input().split())
arr = [int(input()) for _ in range(n)]
    
upper = [0] * (h + 1)
lower = [0] * (h + 1)
for i in range(n):
    if i % 2 == 0:
        upper[arr[i]] += 1
    else:
        lower[arr[i]] += 1

for i in range(h - 1, 0, -1):
    upper[i] += upper[i + 1]
    lower[i] += lower[i + 1]

min_cnt = n
total_cnt = 0
for i in range(1, h + 1): # 500_000
    temp_cnt = upper[h - i + 1] + lower[i]

    if temp_cnt < min_cnt:
        min_cnt = temp_cnt
        total_cnt = 1
    elif temp_cnt == min_cnt:
        total_cnt += 1

print(f'{min_cnt} {total_cnt}')