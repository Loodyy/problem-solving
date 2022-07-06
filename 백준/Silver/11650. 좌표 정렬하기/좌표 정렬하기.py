import sys
input = sys.stdin.readline

n = int(input())
pos = [list(map(int, input().split())) for _ in range(n)]
[print(*p) for p in sorted(pos)]