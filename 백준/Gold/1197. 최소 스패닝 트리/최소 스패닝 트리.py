import heapq

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent[parent[x]]
    return parent[x]

def union_parent(a, b):
    a, b = parent[a], parent[b]
    if a < b: parent[b] = a
    else: parent[a] = b

def solve(src):

    result = 0

    mst = [src]
    q = []
    for e in graph[src]:
        heapq.heappush(q, e)

    while q:
        cost, a, b = heapq.heappop(q)
        if parent[a] != parent[b]:
            union_parent(a, b)
            mst.append(b)
            result += cost
            for cost, a, b in graph[b]:
                heapq.heappush(q, (cost, a, b))
        if len(mst) == v:
            break
    
    print(result)
    return

if __name__ == "__main__":

    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b, cost = map(int, input().split())
        graph[a].append((cost, a, b))
        graph[b].append((cost, b, a))
    parent = list(range(v+1))

    solve(1)
