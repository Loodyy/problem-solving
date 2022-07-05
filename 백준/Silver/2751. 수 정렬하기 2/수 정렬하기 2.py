import sys
input = sys.stdin.readline
[print(x) for x in sorted([int(input()) for _ in range(int(input()))])]