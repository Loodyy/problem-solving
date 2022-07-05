from collections import deque

def solve():
    idxs = deque()
    for i in range(n):
        idxs.append((arr[i], i))
    
    arr.sort()
    cnt = 0
    while True:
        elem, idx = idxs.popleft()
        if arr and arr[-1] != elem:
            idxs.append((elem, idx))
        else:
            cnt += 1
            arr.pop()
            if m == idx:
                return cnt
            
k = int(input())

for _ in range(k):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve())