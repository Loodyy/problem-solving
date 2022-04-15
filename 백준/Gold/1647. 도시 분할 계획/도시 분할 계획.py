import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a, b = find_parent(a), find_parent(b)
    if a < b: parent[b] = a
    else: parent[a] = b

def solve():
    result = 0
    union_cnt = 0

    max = 0
    for edge in arr:
        if union_cnt == v-1:
            break
        cost, a, b = edge
        if find_parent(a) != find_parent(b):
            union_parent(a, b)
            result += cost
            union_cnt += 1
            max = cost

    result -= max    

    print(result)
    return

if __name__ == "__main__":

    v, e = map(int, input().split())
    arr = []
    for _ in range(e):
        temp = list(map(int, input().split()))
        arr.append([temp[2], temp[0], temp[1]])
    arr.sort()

    parent = [0] * (v+1)
    for i in range(v+1):
        parent[i] = i

    solve()