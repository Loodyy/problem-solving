n, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ctrl = [list(map(int, input().split())) for _ in range(c)]

result = 0
dir = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
dig = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
clouds = []
for i in range(n-2, n):
    for j in range(2):
        clouds.append([j, i])
visited = [[False for _ in range(n)] for _ in range(n)]
def move(x, y, idx, dist):
    dx = x + dist * dir[idx][0]
    dy = y + dist * dir[idx][1]
    return dx%n, dy%n

def solve():
    global clouds
    global visited
    
    for c in ctrl:
        for cloud in clouds:
            cloud[0], cloud[1] = move(cloud[0], cloud[1], c[0]-1, c[1])
            arr[cloud[1]][cloud[0]] += 1
            visited[cloud[1]][cloud[0]] = True
            #temp.append([cloud[0], cloud[1]])
        for cloud in clouds:
            x, y = cloud[0], cloud[1]
            for d in dig:
                dx, dy = d[0], d[1]
                if 0 <= x + dx < n and 0 <= y + dy < n and arr[y+dy][x+dx] > 0:
                    arr[y][x] += 1
        #여기서 부터 시간초과 -> visited 쓰면 되네
        clouds = []                        
        for i in range(n):
            for j in range(n):
                if arr[i][j] >= 2 and visited[i][j] == False:
                    arr[i][j] -= 2
                    clouds.append([j, i])
                visited[i][j] = False
            
    result = sum(map(sum, arr))
    print(result)

solve()


        

