from collections import deque

def solve():
    kx = -1
    result = 0

    while True:
        kx += 1

        if kx == m:
            print(result)
            return

        # 해당 열에서 가장 y축이 높은 상어 잡기
        check = False 
        for i in range(n):
            if check:
                break
            for shark in q:
                if kx == shark[0] and i == shark[1]:
                    result += shark[4] # shark's weight
                    q.remove(shark)
                    check = True
                    break
        
        # 상어 이동
        while q:
            x, y, s, d, w = q.pop()
            
            width = n if 0 <= d <= 1 else m 
            # 6: 10, 20 | 4: 6, 12 | 5: 8, 16  (2*n-2)
            for _ in range(s%(2*width-2)):
                dx, dy = dir[d][0], dir[d][1]
                if 0 <= x+dx < m and 0 <= y+dy < n:
                    x, y = x+dx, y+dy
                else:
                    if 0 <= d <= 1:
                        d = 1 if d == 0 else 0
                    else:
                        d = 2 if d == 3 else 3
                    dx, dy = dir[d][0], dir[d][1]
                    x, y = x+dx, y+dy
            temp.append([x, y, s, d, w])
            
        # 이동 후
        arr = [[0 for _ in range(m)] for _ in range(n)]
        tmp = []
        temp.sort(key = lambda x: x[4], reverse=True)
        for shark in temp:
            if not arr[shark[1]][shark[0]]:
                arr[shark[1]][shark[0]] = shark[4]
            else: tmp.append(shark)

        for shark in tmp: temp.remove(shark)

        for _ in range(len(temp)): q.append(temp.pop())

if __name__ == "__main__":
    n, m, num = map(int, input().split())
    q = deque()
    temp = []
    for _ in range(num):
        y, x, speed, direction, weight = map(int, input().split())
        q.append([x-1, y-1, speed, direction-1, weight])

    dir = [(0, -1), (0, 1), (1, 0), (-1, 0)]


    solve()