T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    res = 1
    for i in range(N):
        res = res * (M-i) / (i+1)  
    print(int(res))