import sys
import heapq
input = sys.stdin.readline

q = []
N = int(input())
for _ in range(N):
    cmd = int(input())
    if cmd == 0:
        out = 0
        if q: out = -heapq.heappop(q)
        print(out)
    else:
        heapq.heappush(q, -cmd)