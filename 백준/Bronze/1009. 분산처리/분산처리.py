import sys
input = sys.stdin.readline

k = int(input())

for _ in range(k):
    a, b = map(int, input().split())
    num = pow(a, b, 10)
    
    res = num if num != 0 else 10
    print(res)