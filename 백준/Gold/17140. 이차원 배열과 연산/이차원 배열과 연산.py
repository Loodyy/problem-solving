def solve():

    nx, ny = 3, 3
    cnt = 0
    while arr[r-1][c-1] != k:
        if cnt > 100:
            print(-1)
            return 
        if ny >= nx: #R
            for i in range(ny):
                temp = []
                for j in range(nx):
                    now, arr[i][j] = arr[i][j], 0
                    temp.append(now)
                
                sorted = sort(temp, nx, 0)
                if not j: 
                    nx = len(sorted) if nx <= 100 else 100
                else: nx = max(nx, len(sorted)) # 첫 루프때를 nx로 하고 뒤에 max로 업데이트 해줘야 함

                for j in range(len(sorted)):
                    arr[i][j] = sorted[j]
        else: #C
            for i in range(nx):
                temp = []
                for j in range(nx):
                    now, arr[j][i] = arr[j][i], 0
                    temp.append(now)
                sorted = sort(temp, 0, ny)
                if not j:
                    ny = len(sorted) if ny <= 100 else 100
                else: ny = max(ny, len(sorted))
                if ny > 100: ny = 100
                for j in range(len(sorted)):
                    arr[j][i] = sorted[j]

        cnt += 1

    print(cnt)
    return

def sort(arr, nx, ny):
    c = [0] * (max(arr)+1) # 3 1 1 2 -> 2 1 3 1 1 2 , c = 0 2 1 1
    for x in arr:
        c[x] += 1

    temp = []
    leng = nx if nx > 0 else ny
    for i in range(1, leng+1):
        for j in range(1, len(c)):
            if c[j] == i:
                temp.append(j)
                temp.append(c[j])
    return temp

if __name__ == "__main__":

    arr = [[0] * 100 for _ in range(100)]
    r, c, k = map(int, input().split()) # arr[r][c] = k
    for i in range(3):
        temp = list(map(int, input().split()))
        for j in range(3):
            arr[i][j] = temp[j]

    solve()



