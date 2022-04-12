import heapq
INF = int(1e9)

def solve(src, dst):

    q = []
    distance[src] = 0
    heapq.heappush(q, (0, src))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            target, cost = i[0], dist+i[1]
            if cost < distance[target]:
                distance[target] = cost
                heapq.heappush(q, (cost, target))   

    print(distance[dst])
    return
    

if __name__ == "__main__":
    n = int(input())
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    m = int(input())
    for _ in range(m):
        temp = list(map(int, input().split()))
        graph[temp[0]].append((temp[1], temp[2])) # target, cost
    src, dst = map(int, input().split())

    solve(src, dst)