import sys
sys.setrecursionlimit(int(1e5))

def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for i in graph[x]:
        if c[i]:
            continue
        parent[i] = x
        dfs(i, depth+1)

def solve(a, b):

    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]
    
    print(a)
    return

if __name__ == "__main__":

    t = int(input())
    for _ in range(t):

        n = int(input())
        graph = [[] for _ in range(n+1)]
        check = [0] * (n+1)
        parent = list(range(n+1))
        d = [0] * (n+1)
        c = [0] * (n+1)

        for _ in range(n-1):
            a, b = map(int, input().split())
            graph[a].append(b)
            check[b] += 1
        
        for i in range(1, n+1): # find root node
            if not check[i]:
                root = i 

        a, b = map(int, input().split())
        dfs(root, 0)
        solve(a, b)