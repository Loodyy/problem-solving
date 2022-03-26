import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

r, c = map(int, input().split())

arr = []
birus = []
room = []
for i in range(r):
    temp = list(map(int, input().split()))
    for j in range(c):
        if temp[j] == 2:
            birus.append((j, i)) # x, y
        elif temp[j] == 0:
            room.append((j, i))
    arr.append(temp)

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
list = list(combinations(room, 3))

def bfs(arr):
    visited = [[False for _ in range(c)] for _ in range(r)]
    q = deque()
    for b in birus:
        x, y = b[0], b[1]
        visited[y][x] = True
        q.append((x, y))

    while q:
        x, y = q.popleft()
        for d in dir:
            dx, dy = d[0], d[1]
            tx = x + dx
            ty = y + dy
            if 0 <= tx < c and 0 <= ty < r\
                and arr[ty][tx] != 1 and visited[ty][tx] == False:
                arr[ty][tx] += 2
                visited[ty][tx] = True
                q.append((tx, ty))
        
    check = 0
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 0:
                check += 1

    return check

def solve():
    result = []
    for x in list:
        temp = deepcopy(arr)
        for y in x:
            a, b = y[0], y[1]
            temp[b][a] = 1
        result.append(bfs(temp))
    
    return max(result)

print(solve())


