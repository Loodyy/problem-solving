import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    checked[x][y] = True
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not checked[nx][ny] and height[nx][ny] > water_level:
            dfs(nx, ny)

n = int(input())
height = [list(map(int, input().split())) for _ in range(n)]

max_safe_area = 0
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for water_level in range(max(map(max, height))+1):
    checked = [[False]*n for _ in range(n)]
    safe_area = 0
    for i in range(n):
        for j in range(n):
            if not checked[i][j] and height[i][j] > water_level:
                dfs(i, j)
                safe_area += 1
    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)
