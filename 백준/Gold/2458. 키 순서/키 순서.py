INF = int(1e9)

def solve():

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j: dist[i][j] = 0

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    result = 0
    for i in range(1, n+1):
        s, b = 0, 0
        for j in range(1, n+1):
            if 0 < dist[j][i] < INF: s += 1
            if 0 < dist[i][j] < INF: b += 1 
        if s+b == n-1: result += 1

    print(result)
    return

if __name__ == "__main__":

    n, m = map(int, input().split())
    dist = [[INF] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        dist[a][b] = 1

    solve()
