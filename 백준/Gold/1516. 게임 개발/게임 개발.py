from collections import deque

def solve(n, arr):
    total = ""

    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    cost = [0] * (n+1)

    for i, x in enumerate(arr):
        c, pre = x[0], x[1:-1]
        cost[i+1] = c
        for y in pre:
            graph[y].append(i+1)
            indegree[i+1] += 1
    
    # topologic sort
    total = [0] * (n+1)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        total[now] += cost[now]

        for next in graph[now]:
            indegree[next] -= 1
            total[next] = max(total[next], total[now])
            if indegree[next] == 0:
                q.append(next)

    for x in total[1:]:
        print(x)
    return

def main():

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    solve(n, arr)

if __name__ == "__main__":

    main()
