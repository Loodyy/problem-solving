def solve(x, y):

    parent = [0] * (n+1)
    end = [1]
    idxs = tree()
    for i in range(1, 2*n):
        now = idxs[i]
        e = end[-1]
        if end[-1] != now:
            graph[e].append(now)
            parent[now] = e
            end.append(now)
        else:
            end.pop()

    dfs(1, 0)
    x, y = idxs[x], idxs[y]

    while d[x] != d[y]:
        if d[x] < d[y]: y = parent[y]
        else: x = parent[x]

    while x != y:
        x, y = parent[x], parent[y]
    
    for i in range(n*2):
        if idxs[i] == x:
            print(i+1, end=' ')
    return

def tree():
    idxs = []

    idx = 1
    end = []
    for x in arr:
        if not x: 
            idxs.append(idx)
            end.append(idx)
            idx += 1
        else: idxs.append(end.pop())
    return idxs

def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for i in graph[x]:
        if not c[i]:
            dfs(i, depth+1)

if __name__ == "__main__":

    n = int(input())
    arr = list(map(int, str(input())))
    x, y = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    c = [0] * (n+1)
    d = [0] * (n+1)
 
    solve(x-1, y-1)

    
