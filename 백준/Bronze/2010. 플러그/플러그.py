import sys
input = sys.stdin.readline

n = int(input())
print(sum([int(input()) for _ in range(n)]) - (n-1))