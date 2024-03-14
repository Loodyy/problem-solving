from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    temp = list(map(int, input().split()))
    for j, x in enumerate(temp):
        if x == 1:
            graph[i].append(j+1)

def bfs(src):
    q = deque()
    q.append(src)
    visited = [False] * (n+1)
    # visited[src] = True
    while q:
        x = q.popleft()
        for y in graph[x]:
            if not visited[y]:
                visited[y] = True
                q.append(y)

    return visited[1:]

for i in range(1, n+1):
    print(*[int(b) for b in bfs(i)])