from collections import deque

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            tx, ty = x+dx, y+dy
            if is_range(tx, ty):
                visited[ty][tx] = visited[y][x] + 1
                q.append((tx, ty))

    return visited[r-1][c-1]

def is_range(x, y):
    return 0 <= x < c and 0 <= y < r and visited[y][x] == 0 and board[y][x] == "1"

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

print(bfs())