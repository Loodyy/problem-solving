import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

def round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

if N == 0:
    print(0)
else:
    cut = round(N * 0.15)
    A.sort()
    avg = round(sum(A[cut:N-cut]) / (N-2*cut))
    print(avg)