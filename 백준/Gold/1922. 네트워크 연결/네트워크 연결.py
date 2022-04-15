def solve():
    result = 0

    for edge in arr:
        cost, a, b = edge
        if find_parent(a) != find_parent(b):
            result += cost
            union_parent(a, b)

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

    v = int(input())
    e = int(input())
    arr = []
    for _ in range(e):
        temp = list(map(int, input().split()))
        arr.append([temp[2], temp[0], temp[1]])
    arr.sort()

    parent = [0] * (v+1)
    for i in range(1, v+1):
        parent[i] = i

    solve()