from collections import deque

n, m = int(input()), int(input())
conn = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    conn[a].append(b)
    conn[b].append(a)
visited = [False] * (n+1)

q = deque([1])
visited[1] = True
while q:
    now = q.popleft()
    for next in conn[now]:
        if not visited[next]:
            visited[next] = True
            q.append(next)

print(visited.count(True)-1)