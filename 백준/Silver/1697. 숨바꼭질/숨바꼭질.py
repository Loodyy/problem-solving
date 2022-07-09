from collections import deque

n, k = map(int, input().split())
q = deque()
q.append([k, 0])
visited = set()
while q:
    now, t = q.popleft()
    if now in visited:
        continue
    visited.add(now)

    if now == n:
        print(t)
        break

    if now > n:
        if now%2 == 0:
            q.append([now//2, t+1])
        q.append([now-1, t+1])
    q.append([now+1, t+1])