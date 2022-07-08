from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    q = deque([start])
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n+1)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        visited[i] = True
        cnt += 1
        bfs(i)

print(cnt)