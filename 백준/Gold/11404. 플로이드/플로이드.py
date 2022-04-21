INF = int(1e9)

def solve():

    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                distance[a][b] = 0
                
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
    
    for x in range(1, n+1):
        for y in range(1, n+1):
            result = distance[x][y] if distance[x][y] != INF else 0 
            print(result, end=' ')
        print()
    return

if __name__ == "__main__":

    n = int(input())
    m = int(input())
    distance = [[INF] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b, cost = map(int, input().split())
        distance[a][b] = min(distance[a][b], cost)
 
    solve()
