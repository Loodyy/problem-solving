from collections import deque

def solve():

    dp = [0 for _ in range(n+1)]

    q = deque()
    for i in range(1, n+1):
        if not indegree[i]:
            q.append(i)
            dp[i] = require[i-1]

    while q:
        now = q.popleft()
        if now == target:
            break
        
        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[now] + require[i-1], dp[i])
            if not indegree[i]:
                q.append(i)

    print(dp[target])
    return

if __name__ == "__main__":

    t = int(input())
    
    for _ in range(t):
        n, k = map(int, input().split())
        require = list(map(int, input().split()))
        indegree = [0] * (n+1)
        graph = [[] for _ in range(n+1)]
        for _ in range(k):
            a, b = map(int, input().split())
            graph[a].append(b)
            indegree[b] += 1
        target = int(input())

        solve()
