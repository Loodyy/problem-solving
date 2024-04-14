from collections import deque

N, M = map(int, input().split())
S = None
A = []
for i in range(N):
    temp = list(input())
    for j in range(M):
        if temp[j] == "I":
            S = (i, j)
    A.append(temp)

ans = 0
q = deque([S])
visited = [[False] * M for _ in range(N)]
visited[S[0]][S[1]] = True

while q:
    y, x = q.popleft()
    if A[y][x] == "P":
        ans += 1
    for tx, ty in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + tx, y + ty
        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and A[ny][nx] != "X":
            visited[ny][nx] = True
            q.append((ny, nx))

print(ans if ans > 0 else "TT")