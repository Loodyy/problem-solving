import heapq

def solve(src):
    q = []
    heapq.heappush(q, (0, src))
    distance = [float('inf')] * (n + 1)
    distance[src] = 0

    while q:
        dist, curr = heapq.heappop(q)
        if distance[curr] < dist:
            continue
        for next in graph[curr]:
            cost = dist + next[1]
            if cost < distance[next[0]]:
                node = next[0]
                distance[node] = cost
                heapq.heappush(q, (cost, node))

    for i in range(1, n + 1):
        short_paths[src].append((i, distance[i]))

n, m, r = map(int, input().split())
item_cnts = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
short_paths = [[] for _ in range(n + 1)]

for _ in range(r):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

for i in range(1, n + 1):
    solve(i)

max_item = -1
for i in range(1, n + 1):
    item = 0
    for node, dist in short_paths[i]:
        if dist <= m:
            item += item_cnts[node - 1]
    max_item = max(max_item, item)

print(max_item)