import sys
sys.setrecursionlimit(int(1e5))

def solve():

    result = 0
    for cost, a, b in e:
        if find_parent(a) != find_parent(b):
            union_parent(a, b)
            result += cost

    print(result)
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

    n = int(input())
    parent = list(range(n))
    arr = []
    e = []
    for idx in range(n):
        x, y, z = map(int, input().split())
        arr.append((x, y, z, idx))

    for i in range(3):
        arr.sort(key=lambda x: x[i])
        for j in range(n-1):
            cost = abs(arr[j][i]-arr[j+1][i])
            fir, sec = arr[j][3], arr[j+1][3]
            e.append((cost, fir, sec))

    e.sort()
    solve()

