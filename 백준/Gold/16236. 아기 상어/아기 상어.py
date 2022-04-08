from collections import deque

def solve():
    cnt = 0
    while True:
        idxs = check(shark[2])

        if not len(idxs):
            print(cnt)
            return 

        elif len(idxs) > 0:
            q = deque()
            visited = [[n*n for _ in range(n)] for _ in range(n)]
            a, b = shark[0], shark[1]
            
            visited[b][a] = 0
            q.append([a, b])
            while q:
                x, y = q.pop()
                for d in dir:
                    dx, dy = d[0], d[1]
                    if 0 <= x+dx < n and 0 <= y+dy < n and arr[y+dy][x+dx] <= shark[2]:
                        if visited[y+dy][x+dx] <= visited[y][x] + 1:
                            continue
                        visited[y+dy][x+dx] = visited[y][x] + 1
                        q.append([x+dx, y+dy])

            bool = False
            for idx in idxs:
                if visited[fish[idx][2]][fish[idx][1]] != n*n:
                    bool = True
            if not bool:
                print(cnt)
                return
    
            dist = n*n 
            midx = 0
            for idx in idxs:
                now = fish[idx]
                if visited[now[2]][now[1]] < dist:
                    dist = visited[now[2]][now[1]]
                    midx = idx
            
            mins = [] # 가까운 거리 중복
            mx, my = fish[midx][1], fish[midx][2]
            for idx in idxs:
                if visited[fish[idx][2]][fish[idx][1]] == dist:
                    mins.append(idx)
            
            if len(mins) > 1:
                for min in mins:
                    if my > fish[min][2]:
                        midx = min
                        mx, my = fish[min][1], fish[min][2]
                    elif my == fish[min][2]:
                        if mx > fish[min][1]:
                            midx = min
                            mx, my = fish[min][1], fish[min][2]

            tx, ty = fish[midx][1], fish[midx][2]
            fish.pop(midx)
            arr[ty][tx] = 9
            arr[shark[1]][shark[0]] = 0
            shark[0], shark[1] = tx, ty
            cnt += dist
            shark[3] += 1
            if shark[2] == shark[3]:
                shark[2] += 1
                shark[3] = 0
        

def check(shark_w):
    idxs = []

    for i, x in enumerate(fish):
        if shark_w > x[0]:
            idxs.append(i)

    return idxs

if __name__ == "__main__":
    n = int(input())
    fish = []
    shark = []
    arr = []
    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(n):
            if 0 < temp[j] < 7:
                fish.append([temp[j], j, i])
            elif temp[j] == 9:
                shark = [j, i, 2, 0] # x, y, weigth, eat
        arr.append(temp)
    
    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    solve()
