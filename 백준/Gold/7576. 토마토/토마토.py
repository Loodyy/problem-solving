from collections import deque
import sys
input = sys.stdin.readline


def solve():
    m, n = map(int, input().split())
    arr = []
    q = deque([])
    for y in range(n):
        temp = list(map(int, input().split()))
        for x in range(m):
            if temp[x] == 1:
                q.append((x, y))
        arr.append(temp)
        
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y = q.popleft()
        for i in d:
            a = x + i[0]
            b = y + i[1]
            if 0 <= a < m and 0 <= b < n and arr[b][a] == 0:
                arr[b][a] = arr[y][x] + 1
                q.append((a, b))

    cnt = 0
    for i in arr:
        for j in i:
            if j == 0:
                return -1
        cnt = max(cnt, max(i))

    return cnt - 1

print(solve())