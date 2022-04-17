def solve():
    result = 0

    cnt = 0
    for i in arr:
        a, b, cost = i
        if find_parent(a) != find_parent(b):
            union_parent(a, b)
            result += (cnt*t + cost)
            cnt += 1

    print(result)
    return

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a, b = find_parent(a), find_parent(b)
    if a < b: parent[b] = a
    else: parent[a] = b

if __name__ == "__main__":

    n, m, t = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    arr.sort(key=lambda x: x[2])
    
    parent = list(range(n+1))

    solve()