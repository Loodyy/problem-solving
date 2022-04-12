from dis import dis
import heapq
INF = int(1e9)

def solve(dst):
    result = 0

    back = dijsktra(dst) # x에서 돌아올 때 비용들

    for src in range(1, n+1):
        go = dijsktra(src)
        if result < go[dst] + back[src]:
            result = go[dst] + back[src]

    print(result)
    return

def dijsktra(src):
    distance = [INF] * (n+1)

    q = []
    heapq.heappush(q, (0, src))
    distance[src] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            target, cost = i[0], dist + i[1]
            if cost < distance[target]:
                distance[target] = cost
                heapq.heappush(q, (cost, target))
    
    return distance

if __name__ == "__main__":

    n, m, dst = map(int, input().split())
    
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        temp = list(map(int, input().split()))
        graph[temp[0]].append((temp[1], temp[2])) # dst, cost

    solve(dst)
