import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for i in graph[x]:
        if not c[i]:
            parent[i] = x
            dfs(i, depth+1)
    return

def solve(a, b):

    while d[a] != d[b]:
        if d[a] < d[b]: b = parent[b]
        else: a = parent[a]

    while a != b:
        a, b = parent[a], parent[b]

    print(a)
    return

if __name__ == "__main__":

    n = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    parent = list(range(n+1))
    c = [0] * (n+1)
    d = [0] * (n+1)

    dfs(1, 0)
    
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        solve(a, b)
