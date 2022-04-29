import sys
import heapq
input = sys.stdin.readline

def solve():

    total = 0
    while len(q) > 1:
        fir = heapq.heappop(q)
        sec = heapq.heappop(q)
        new = fir + sec
        total += new
        heapq.heappush(q, new)
        
    print(total)
    return

if __name__ == "__main__":

    n = int(input())
    q = []
    for _ in range(n):
        heapq.heappush(q, int(input()))

    solve()
