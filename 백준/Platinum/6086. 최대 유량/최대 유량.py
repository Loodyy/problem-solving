from collections import deque
INF, MAX = int(1e9), 130

def solve(c, f, graph, src, dst):

    result = 0

    while True:
        v = [-1] * MAX
        q = deque()
        q.append(src)
        while q:
            now = q.popleft()
            for next in graph[now]:
                if c[now][next] > f[now][next] and v[next] == -1:
                    q.append(next)
                    v[next] = now
                    if next == dst: break
        
        if v[dst] == -1: break

        flow = INF
        
        tmp = dst
        while tmp != src:
            flow = min(flow, c[v[tmp]][tmp] - f[v[tmp]][tmp])
            tmp = v[tmp]

        tmp = dst
        while tmp != src:
            f[v[tmp]][tmp] += flow
            f[tmp][v[tmp]] -= flow
            tmp = v[tmp]
        
        result += flow

    print(result)
    return

if __name__ == "__main__":

    e = int(input())
    c = [[0] * MAX for _ in range(MAX)]
    f = [[0] * MAX for _ in range(MAX)]
    graph = [[] * MAX for _ in range(MAX)]
    for _ in range(e):
        a, b, cost = input().split()
        a, b, cost = ord(a), ord(b), int(cost)
        graph[a].append(b)
        graph[b].append(a)
        c[a][b] += cost
        c[b][a] += cost

    solve(c, f, graph, ord("A"), ord("Z"))