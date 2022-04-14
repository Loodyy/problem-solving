from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

def solve():
    result = 0

    a, b = map(int, input().split())

    fir = mst(1) # from 1 ~
    sec = mst(n) # from n ~ 
    com = mst(a)[b]
    result = min(fir[a] + com + sec[b], fir[b] + com + sec[a])
                 # 1~a    a~b    b~n     1~b     b~a    a~n

    if result < INF: print(result)
    else: print(-1) # 경로 없을 때
    return

def mst(src):

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

    return distance

if __name__ == "__main__":

    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        temp = list(map(int, input().split()))
        graph[temp[0]].append([temp[1], temp[2]])
        graph[temp[1]].append([temp[0], temp[2]]) # 양방향

    solve()