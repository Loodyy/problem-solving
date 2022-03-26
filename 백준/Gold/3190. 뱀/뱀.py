import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = int(input())
apple = []
for _ in range(a):
    x, y = map(int, input().split())
    apple.append((y-1, x-1))
c = int(input())
ctrl = []
for _ in range(c):
    x, y = input().split()
    ctrl.append((int(x), y))

map = [[0 for _ in range(n)] for _ in range(n)]
for x in apple:
    map[x[1]][x[0]] = "A"

#상, 우, 하, 좌
d = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def direction(idx, c):
    if c == "L":
        idx = (idx - 1) % 4  
    else:
        idx = (idx + 1) % 4
    return idx

def solve():
    x, y = 0, 0
    q = deque([(x, y)])
    dir = 1
    map[y][x] == 1
    
    cnt = 1
    tidx = 0
    while True:
        c = ctrl[tidx]
        t, nd = c[0], c[1]
        dx, dy = d[dir][0], d[dir][1]
        x, y = x + dx, y + dy
        if 0 <= x < n and 0 <= y < n and map[y][x] != 1:
            if map[y][x] == 0:
                tx, ty = q.popleft()
                map[ty][tx] = 0
            map[y][x] = 1
            q.append((x, y))
            if cnt == t:
                dir = direction(dir, nd)
                if tidx < len(ctrl)-1:
                    tidx += 1
            cnt += 1
        else:
            return cnt

print(solve())