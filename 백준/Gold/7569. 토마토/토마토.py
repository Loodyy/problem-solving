from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())

arr = []
q = deque()
for z in range(h):
    temp = []
    for y in  range(n):
        temp.append(list(map(int, input().split())))
        for x in range(m):
            if temp[y][x] == 1:
                q.append((z, y, x)) 
    arr.append(temp)

d = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

def solve():
    
    while q:  
        a, b, c = q.popleft()
        for x, y, z in d:
            z += a
            y += b
            x += c
            if 0 <= x < m and 0 <= y < n and 0 <= z < h and arr[z][y][x] == 0:
                q.append((z, y, x))
                arr[z][y][x] = arr[a][b][c] + 1

    cnt = 0
    for i in arr:
        for j in i:
            if 0 in j:
                return -1
            cnt = max(cnt, max(j))
    return cnt - 1  # 요소의 시작이 1이라 하루 지나면 max = 2 -> day = cnt - 1 

print(solve())
    
    

    