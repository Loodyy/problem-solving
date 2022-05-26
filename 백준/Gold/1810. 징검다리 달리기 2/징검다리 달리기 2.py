### 37993597번 코드 참조 ### 

import heapq
INF = int(1e9)

def solve(n, f, dic):

    if f == 0:
        return 0

    q = []
    heapq.heappush(q, (0, 0, 0)) # cost, x, y
    dic[(0, 0)] = 0

    result = []

    while q:
        dist, x, y = heapq.heappop(q)
        for i in range(-2, 3):
            for j in range(-2, 3):
                tx, ty = x+j, y+i
                if dic.get((tx, ty)):
                    d = ((x-tx)**2 + (y-ty)**2)**(1/2)
                    if dist+d < dic[(tx, ty)]:
                        dic[(tx, ty)] = dist+d
                        heapq.heappush(q, (dist+d, tx, ty))
                        if ty == f: result.append(round(dist+d))

    if len(result):
        return min(result)
    else: return -1

if __name__ == "__main__":

    n, f = map(int, input().split())
    dic = {}
    for i in range(n):
        a, b = map(int, input().split())
        dic[(a, b)] = INF

    print(solve(n, f, dic))