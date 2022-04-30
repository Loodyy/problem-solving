import sys
input = sys.stdin.readline

def solve():

    result = 0
    for edge in arr:
        a, b, cost= edge
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
        arr = [list(map(int, input().split())) for _ in range(n)]
        parent = list(range(h+1))
        total = sum(i[2] for i in arr)
        arr.sort(key=lambda x: x[2])

        solve()
