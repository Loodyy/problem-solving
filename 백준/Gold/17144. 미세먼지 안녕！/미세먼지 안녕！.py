from collections import deque

def solve(t):
    cnt = 0

    while True:
        if cnt == t:
            print(sum(map(sum, arr))+2)
            return

        # 미세먼지
        arr_temp = [[0 for _ in range(m)] for _ in range(n)] 
        while q:
            x, y = q.pop()
            dcnt = 0
            di = []
            for d in dir:
                tx, ty = x+d[0], y+d[1]
                if [tx, ty] not in air and 0 <= tx < m and 0 <= ty < n:                    
                    dcnt += 1
                    di.append(d)
            plus = arr[y][x] // 5
            arr_temp[y][x] -= plus * dcnt
            for d in di:
                tx, ty = x+d[0], y+d[1]
                arr_temp[ty][tx] += plus
        
        for i in range(n):
            for j in range(m):
                arr[i][j] += arr_temp[i][j] 
        # 확산

        # clean
        aidx = air[0][1]
        for i in range(aidx, 0, -1):
            arr[i][0] = arr[i-1][0]
        for i in range(aidx+1, n-1):
            arr[i][0] = arr[i+1][0]
        arr[aidx][0], arr[aidx+1][0] = -1, -1
        
        for i in range(m-1):
            arr[0][i] = arr[0][i+1]
            arr[n-1][i] = arr[n-1][i+1]
        
        for i in range(aidx):
            arr[i][m-1] = arr[i+1][m-1]
        for i in range(n-1, aidx+1, -1):
            arr[i][m-1] = arr[i-1][m-1]

        for i in range(m-1, 1, -1):
            arr[aidx][i] = arr[aidx][i-1]
            arr[aidx+1][i] = arr[aidx+1][i-1]
        arr[aidx][1], arr[aidx+1][1] = 0, 0

        # next stage deque
        for i in range(n):
            for j in range(m):
                if arr[i][j] > 4:
                    q.append([j, i])

        cnt += 1

if __name__ == "__main__":
    n, m, t = map(int, input().split())
    arr = []
    air = []
    q = deque()
    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(m):
            if temp[j] == -1:
                air.append([j, i])
            elif temp[j] > 4:
                q.append([j, i])
        arr.append(temp)

    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    solve(t)