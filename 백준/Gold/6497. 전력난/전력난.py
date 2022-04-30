import heapq

def solve():

    result = 0
    for edge in arr:
        cost, a, b = edge
        if find_parent(a) != find_parent(b):
            union_parent(a, b)
            result += cost

    print(total-result)
    return

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a, b = parent[a], parent[b]
    if a < b: parent[b] = a
    else: parent[a] = b

if __name__ == "__main__":

    while True:
        h, n = map(int, input().split())
        if not h and not n:
            break
        arr = []
        parent = list(range(n+1))
        total = 0
        for _ in range(n):
            a, b, cost = map(int, input().split())
            total += cost
            arr.append((cost, a, b))
        arr.sort()

        solve()
