import sys, heapq
input = sys.stdin.readline

Q = []
N = int(input())
for _ in range(N):
    num = int(input())
    if num == 0:
        if len(Q) == 0:
            print(0)
            continue
        number, sign = heapq.heappop(Q)
        if sign == 0:
            number *= -1
        print(number)
    else:
        sign = 0 if num < 0 else 1 # -: 0, +: 1
        heapq.heappush(Q, (abs(num), sign))