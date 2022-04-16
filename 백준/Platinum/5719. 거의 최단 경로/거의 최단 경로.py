from collections import deque
import heapq
import sys
input = sys.stdin.readline
INF = int(1e10)

def solve(src, dst):
    
    distance = dijstra(src, dst)
    
    temp = bfs(src, dst, distance)

    for tmp in temp:
        s, d = tmp[0], tmp[1]
        for j in graph[s]:
            if j[0] == d:
                graph[s].remove(j)

    distance = [INF] * n      
    result = dijstra(src, dst)[dst]
    if result != INF: print(result)
    else: print(-1)
    return

def dijstra(src, dst):

    distance = [INF] * n
    distance[src] = 0
    q = []
    heapq.heappush(q, [0, src])

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            target, cost = i[0], i[1] + dist
            if cost < distance[target]:
                distance[target] = cost
                heapq.heappush(q, [cost, target])

    return distance

def bfs(src, dst, distance):

    temp = []

    q = deque()
    q.append(dst)
    
    while q:
        now = q.popleft()
        if now == src:
            continue
        for i in graphR[now]:
            pre, cost = i[0], i[1]
            if distance[pre] + cost == distance[now]: # 최단거리 경로
                if (pre, now) not in temp:
                    temp.append((pre, now))
                    q.append(pre)
    return temp

if __name__ == "__main__":

    while True:
        n, m = map(int, input().split())
        if not n and not m:
            break
        src, dst = map(int, input().split())
        graph = [[] for _ in range(n)]
        graphR = [[] for _ in range(n)]
        for _ in range(m):
            temp = list(map(int, input().split()))
            graph[temp[0]].append([temp[1], temp[2]])
            graphR[temp[1]].append([temp[0], temp[2]])

        solve(src, dst)