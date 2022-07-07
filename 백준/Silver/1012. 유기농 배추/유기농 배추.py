import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[y][x] = True
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            tx, ty = x+dx, y+dy
            if is_range(tx, ty) and visited[ty][tx] == False:
                visited[ty][tx] = True
                q.append((tx, ty))

def is_range(x, y):
    return 0 <= x < c and 0 <= y < r and arr[y][x] == 1

TK = int(input())
for _ in range(TK):
    c, r, k = map(int, input().split())
    
    arr = [[0] * c for _ in range(r)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    visited = [[False] * c for _ in range(r)]
    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    cnt = 0
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 1 and visited[i][j] == False:
                bfs(j, i)
                cnt += 1

    print(cnt)