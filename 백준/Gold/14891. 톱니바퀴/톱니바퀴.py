def calc(c):
    gidx = c[0]-1
    didx = c[1]
    temp = [0, 0, 0] # check magnet
    for i in range(3):
        if arr[i][2] != arr[i+1][6]:
            temp[i] = 1

    rotate(gidx, didx)

    while 0 <= gidx - 1:
        if temp[gidx-1] == 1:
            gidx -= 1
            didx *= -1
            rotate(gidx, didx)
        else: break

    gidx = c[0]-1       
    didx = c[1]
    while gidx + 1 < 4:        
        if temp[gidx] == 1:
            gidx += 1
            didx *= -1
            rotate(gidx, didx)
        else: break
   
    return

def rotate(idx, d):
    temp = [0] * 8
    if d == 1: # clock wise
        for i in range(7):
            temp[i+1] = arr[idx][i]
        temp[0] = arr[idx][7]
    else: # counter clock wise
        for i in range(1, 8):
            temp[i-1] = arr[idx][i]
        temp[7] = arr[idx][0]

    for i in range(8):
        arr[idx][i] = temp[i]

def solve():
    result = 0

    for c in ctrl:
        calc(c)

    for i in range(4):
        if arr[i][0] == 1:
            result += 2**(i)
    print(result)
    return 

if __name__ == "__main__":
    arr = [list(map(int, str(input()))) for _ in range(4)] # 좌idx: 6, 우idx: 2
    n = int(input()) 
    ctrl = [list(map(int, input().split())) for _ in range(n)] # 1 시계, -1 반시계

    solve()
