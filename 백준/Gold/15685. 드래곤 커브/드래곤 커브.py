def solve():
    result = 0

    for curv in curvs:
        x, y, d, g = curv
        arr[y][x] = 1

        dirs = [d] # [0] -> [0,1] -> [0,1,2,1], [0, 1, 2, 1, ]
        for _ in range(g):
            for i in range(len(dirs)-1, -1, -1):
                dirs.append((dirs[i]+1)%4) # 역순으로 90도 회전된 방향을 추가
        
        for d in dirs:
            x, y = x+dir[d][0], y+dir[d][1]
            if 0 <= x < 101 and 0 <= y < 101:
                arr[y][x] = 1
    
    for i in range(100):
        for j in range(100):
            if arr[i][j] and arr[i][j+1] and arr[i+1][j] and arr[i+1][j+1]:
                result += 1

    print(result)
    return 

if __name__ == "__main__":

    n = int(input())
    curvs = [list(map(int, input().split())) for _ in range(n)]
    arr = [[0]*101 for _ in range(101)]

    dir = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    
    solve()
    

    

    
