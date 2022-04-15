from collections import deque

def bfs(start):

    visited = [False] * (n+1)

    q = deque()
    q.append(start)
    visited[start] = True
    
    while q:
        now = q.popleft()
        print(now, end=' ')
        graph[now].sort()
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True    
    return

def dfs(start):

    visited[start] = True
    print(start, end=' ')
    graph[start].sort()
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
    return

if __name__ == "__main__":

    n, m, start = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        temp = list(map(int, input().split()))
        graph[temp[0]].append(temp[1])
        graph[temp[1]].append(temp[0])

    visited = [False] * (n+1)

    dfs(start)
    print()
    bfs(start)
    