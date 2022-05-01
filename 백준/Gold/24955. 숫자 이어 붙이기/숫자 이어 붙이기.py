import sys
from collections import deque

def solve(): 

    dfs(1, 0)
    
    for a, b in case: # 1000
        left, right = deque(), deque()

        while d[a] != d[b]:

            if d[a] < d[b]: # 1000
                right.appendleft(arr[b-1])
                b = parent[b]
                
            elif d[a] > d[b]: 
                left.append(arr[a-1])
                a = parent[a]
        
        while a != b:
            left.append(arr[a-1])
            right.appendleft(arr[b-1])
            a, b = parent[a], parent[b]
        left.append(arr[a-1])
            

        left.extend(right)
        res = int("".join(list(map(str, left)))) % 1000000007

        print(res)
    return

def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for i in graph[x]:
        if not c[i]:
            parent[i] = x
            dfs(i, depth+1)

if __name__ == "__main__":

    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = list(range(n+1))
    graph = [[] * (n+1) for _ in range(n+1)]
    c = [False] * (n+1)
    d = [False] * (n+1)

    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    case = [list(map(int, input().split())) for _ in range(q)]

    solve()
