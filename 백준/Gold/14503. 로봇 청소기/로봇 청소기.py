import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    y, x, ndir = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    result = 1

    arr[y][x] = 2
    idx = ndir

    while True:
        check = False
        for _ in range(4):
            idx = (idx-1)%4
            temp = dir[idx]
            tx, ty = x+temp[0], y+temp[1]
            
            if arr[ty][tx] == 0:
                arr[ty][tx] = 2
                result += 1
                x, y = tx, ty
                check = True
                break

        if check == False:
            tx, ty = x-temp[0], y-temp[1]
            if arr[ty][tx] == 2:
                x, y = tx, ty
            else:
                break
    
    return print(result)

if __name__ == "__main__":
    solve()