from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
src = None
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        if temp[j] == 2:
            src = (i, j)
    board.append(temp)

q = deque([src])
visited = [[0] * M for _ in range(N)]
visited[src[0]][src[1]] = 1
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while q:
    y, x = q.popleft()
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and board[ny][nx] == 1 and visited[ny][nx] == 0:
            visited[ny][nx] = visited[y][x] + 1
            q.append((ny, nx))

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            if board[i][j] == 1:
                print(-1, end=' ')
            else:
                print(0, end=' ')
        else:
            print(visited[i][j]-1, end=' ')
    print()