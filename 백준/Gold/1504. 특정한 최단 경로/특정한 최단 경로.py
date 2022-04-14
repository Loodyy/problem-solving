from collections import deque
INF = int(1e9)

def solve():
    result = 0

    a, b = map(int, input().split())

    result = mst(a, b) + min(mst(1, a) + mst(b, n), mst(1, b) + mst(a, n)) # a, b 순서 무시

    if result < INF: print(result)
    else: print(-1) # 경로 없을 때
    return

def mst(src, dst):

    distance = [INF] * (n+1)

    q = deque()
    q.append((0, src))
    distance[src] = 0
    
    while q:
        dist, now = q.pop()
        if dist > distance[now]:
            continue
        for i in graph[now]:
            target, cost = i[0], dist + i[1], 
            if distance[target] > cost:
                distance[target] = cost
                q.append((cost, target))

    return distance[dst]

if __name__ == "__main__":

    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        temp = list(map(int, input().split()))
        graph[temp[0]].append([temp[1], temp[2]])
        graph[temp[1]].append([temp[0], temp[2]]) # 양방향

    solve()