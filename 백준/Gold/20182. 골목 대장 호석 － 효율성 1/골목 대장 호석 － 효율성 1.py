import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


def solve():

    l, r = 0, max_c
    result = INF
    while l <= r:
        limit = (l+r)//2

        q = []
        heapq.heappush(q, (0, src))
        distance = [INF] * (n+1)
        distance[src] = 0
        find = False
        while q:
            if find: break
            dist, now = heapq.heappop(q)
            if dist >= total or dist > distance[now]: 
                continue
            for i in graph[now]:
                next, cost = i[0], i[1]+dist
                if i[1] > limit:
                    continue
                if cost <= total and cost < distance[next]:
                    distance[next] = cost
                    heapq.heappush(q, (cost, next))
                    if next == dst:
                        find = True

        if find:
            result = min(result, limit) 
            r = limit-1
        else: l = limit+1
    
    result = result if result != INF else -1
    print(result)
    return

if __name__ == "__main__":

    n, m, src, dst, total = map(int, input().split()) # n: 100,000
    graph = [[] for _ in range(n+1)]
    max_c = 0
    for _ in range(m): # 500,000
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
        max_c = max(max_c, c)

    solve()
