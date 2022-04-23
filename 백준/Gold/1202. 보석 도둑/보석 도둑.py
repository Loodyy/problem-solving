import heapq
import sys
input = sys.stdin.readline

def solve():

    result = 0
    
    q = []
    for b in bag:
        while arr and b >= arr[0][0]:
            heapq.heappush(q, -heapq.heappop(arr)[1])

        if q: result += heapq.heappop(q)
        elif not arr: break
    
    print(-result)
    return

if __name__ == "__main__":

    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    bag = [int(input()) for _ in range(k)]
    arr.sort()
    bag.sort()

    solve()
