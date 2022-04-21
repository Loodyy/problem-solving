import sys
input = sys.stdin.readline
INF = int(1e9)

def solve():

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j: dist[i][j] = 0
            else:
                if dist[i][j] != INF:
                    path[i][j].append(i)

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                a, b = dist[i][j], dist[i][k]+dist[k][j]
                if a > b:
                    dist[i][j] = b
                    path[i][j] = path[i][k] + path[k][j]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and dist[i][j] != INF: path[i][j].append(j)

    for i in range(1, n+1):
        for j in range(1, n+1):
            result = dist[i][j] if dist[i][j] != INF else 0
            print(result, end=' ')
        print()

    for i in range(1, n+1):
        for j in range(1, n+1):
            now = path[i][j]
            if not len(now): print(0)
            else:
                print(len(now), end=' ')
                for x in now: print(x, end=' ')
                print()
    return

if __name__ == "__main__":

    n = int(input())
    m = int(input())
    dist = [[INF] * (n+1) for _ in range(n+1)]
    path = [[[] for _ in range(n+1)] for _ in range(n+1)]

    for _ in range(m):
        a, b, cost = map(int, input().split())
        if dist[a][b] > cost: dist[a][b] = cost
 
    solve()
