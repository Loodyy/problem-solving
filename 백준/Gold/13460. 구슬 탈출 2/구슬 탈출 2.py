from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())

arr = []
object = [0] * 2

for i in range(r):
    temp = list(input())
    arr.append(temp)
    for j in range(c):
        if temp[j] == "R": object[0] = (i, j)
        elif temp[j] == "B": object[1] = (i, j)

q = deque()
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[[[False] * c for _ in range(r)] for _ in range(c)] for _ in range(r)] 

def move(x, y, dx, dy):
    cnt = 0
    while arr[x+dx][y+dy] != "#" and arr[x][y] != "O":
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def solve(red, blue):
    rx, ry = red[0], red[1]
    bx, by = blue[0], blue[1]

    q.append((rx, ry, bx, by, 1))

    visited[rx][ry][bx][by] = True

    num = 0
    while q:
        rx, ry, bx, by, num = q.popleft()
        if num > 10:
            break
        for x in d:
            nrx, nry, rcnt = move(rx, ry, x[0], x[1])
            nbx, nby, bcnt = move(bx, by, x[0], x[1])

            if arr[nbx][nby] != "O":
                if arr[nrx][nry] == "O":
                    return num
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= x[0]
                        nry -= x[1]
                    else:
                        nbx -= x[0]
                        nby -= x[1]
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    q.append((nrx, nry, nbx, nby, num + 1))
                    
    return -1

print(solve(object[0], object[1]))

