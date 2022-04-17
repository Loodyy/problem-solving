import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))
INF = int(1e9)

def solve(src, dst):
    
    path = [0] * (n+1)
    
    q = []
    heapq.heappush(q, (0, src))
    distance[src] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            nxt, cost = i[0], i[1] + dist
            if cost < distance[nxt]:
                distance[nxt] = cost
                path[nxt] = now
                heapq.heappush(q, (cost, nxt))

    temp = [dst]
    pathidx = trace(src, dst, path, temp)
    pathidx.reverse()

    print(distance[dst])
    print(len(pathidx))
    for i in pathidx:
        print(i, end=' ')   
    return

def trace(src, dst, path, temp):
    
    if path[dst] == src:
        temp.append(src)
        return temp
    else:
        temp.append(path[dst])
        trace(src, path[dst], path, temp)
        
    return temp
if __name__ == "__main__":

    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for _ in range(m):
        a, b, cost = map(int, input().split())
        graph[a].append([b, cost])

    src, dst = map(int, input().split())

    solve(src, dst)