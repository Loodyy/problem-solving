import sys
input = sys.stdin.readline

n, m, a, b, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ctrl = list(map(int, input().split()))
    
dice = [0, 0, 0, 0, 0, 0]
dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def change(ctrl):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] 
    if ctrl == 1: 
        dice[0], dice[2], dice[3], dice[5] = f, a, c, d
    elif ctrl == 2: 
        dice[0], dice[2], dice[3], dice[5] = c, d, f, a
    elif ctrl == 3: 
        dice[0], dice[1], dice[3], dice[4] = b, d, e, a
    else: 
        dice[0], dice[1], dice[3], dice[4] = e, a, b, d

def solve():
    x, y = b, a
    for c in ctrl:
        t = dir[c-1]
        tx, ty = x + t[0], y + t[1]
        if 0 <= tx < m and 0 <= ty < n:
            change(c)
            if arr[ty][tx] == 0:
                arr[ty][tx] = dice[0] 
            else: 
                dice[0] = arr[ty][tx]
                arr[ty][tx] = 0
            print(dice[3])
            x, y = tx, ty

solve()
    
