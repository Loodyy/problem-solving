import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a, b = find_parent(a), find_parent(b)
    if a < b: parent[b] = a
    else: parent[a] = b

if __name__ == "__main__":

    n, m = map(int, input().split())
    parent = list(range(n+1))
    

    for _ in range(m):
        check, a, b = list(map(int, input().split()))
        if not check: union_parent(a, b)
        else:
            if find_parent(a) != find_parent(b): print("no")
            else: print("yes")
