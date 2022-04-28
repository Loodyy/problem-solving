from collections import deque

def solve():

    cnt = 1
    while True:
        for i, p in enumerate(pos): # 1 ~ k
            x, y = p[0], p[1]          
            for j, c in enumerate(chess[y][x]):
                idx, d = c[0], c[1]
                if idx == i+1:
                    idxs = [] 
                    chunk = list(chess[y][x])[j:]
                    chess[y][x] = deque(list(chess[y][x])[:j])
                    for c in chunk: # x: (idx, d)
                        idxs.append(c[0])
                    tx, ty = x+dir[d][0], y+dir[d][1]
                    
                    if (0 <= tx < n and 0 <= ty < n) and (arr[ty][tx] == 0 or arr[ty][tx] == 1):
                        
                        if arr[ty][tx] == 0:
                            chess[ty][tx].extend(chunk)
                        else:
                            chess[ty][tx].extend(chunk[::-1])
                        move_pos(idxs, d)
                    else:   
                        if d < 3: d = 1 if d == 2 else 2
                        else: d = 3 if d == 4 else 4
                        chunk[0][1] = d
                        
                        tx, ty = x+dir[d][0], y+dir[d][1]

                        if (0 <= tx < n and 0 <= ty < n) and (arr[ty][tx] == 0 or arr[ty][tx] == 1):
                            if arr[ty][tx] == 0:
                                chess[ty][tx].extend(chunk)
                            else:
                                chess[ty][tx].extend(chunk[::-1])
                            move_pos(idxs, d)
                        else: chess[y][x].extend(chunk)

            for i in chess:
                for j in i:
                    if len(j) >= 4:
                        print(cnt)
                        return 
        if cnt > 1000:
            print(-1)
            return 
        cnt += 1

def move_pos(idxs, d):
    for idx in idxs:
        pos[idx-1][0] += dir[d][0] 
        pos[idx-1][1] += dir[d][1]
    return

if __name__ == "__main__":

    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    chess = [[deque() for _ in range(n)] for _ in range(n)]
    pos = []
    for idx in range(k):
        y, x, d = map(int, input().split())
        chess[y-1][x-1].append([idx+1, d])
        pos.append([x-1, y-1])

    dir = [0, (1, 0), (-1, 0), (0, -1), (0, 1)]

    solve()
