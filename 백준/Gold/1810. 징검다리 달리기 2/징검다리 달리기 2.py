import heapq
INF = int(1e9)

def solve(n, f, arr, graph):

    if f == 0:
        return 0

    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, 0))
    distance[0] = 0

    result = []

    while q:
        dist, now = heapq.heappop(q)
        if dist <= distance[now]:
            for v in graph[now]:
                next, cost = v[0], v[1]+dist
                if cost < distance[next]:
                    distance[next] = cost
                    if arr[next][1] == f:
                        result.append(round(cost))
                    heapq.heappush(q, (cost, next))

    if len(result):
        return min(result)
    else: return -1

def check(x, y, nx, ny):
    if abs(x-nx) <= 2 and abs(y-ny) <= 2:
        dist = ((x-nx)**2 + (y-ny)**2)**(1/2)
        return dist
    else:
        return 0

if __name__ == "__main__":

    n, f = map(int, input().split())
    arr = [(0, 0)]
    for i in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))

    arr.sort()
    
    graph = [[] for _ in range(n+1)]
    for i, a in enumerate(arr):
        ax, ay = a
        for j in range(i, n+1):
            bx, by = arr[j]
            if bx - ax > 2:
                break
            d = check(ax, ay, bx, by)
            if d:
                graph[i].append((j, d))
                graph[j].append((i, d))

    print(solve(n, f, arr, graph))
