from collections import deque

def solve():
    
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    result = []

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if not indegree[i]:
                q.append(i)
        
        if len(result) == n:
            for x in result:
                print(x)
            return

    print(0)
    return

if __name__ == "__main__":

    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)

    for _ in range(m):
        temp = list(map(int, input().split()))
        for i in range(1, temp[0]):
            graph[temp[i]].append(temp[i+1])
            indegree[temp[i+1]] += 1

    solve()


