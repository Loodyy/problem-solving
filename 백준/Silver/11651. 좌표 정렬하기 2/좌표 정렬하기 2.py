import sys
input = sys.stdin.readline

pos = [list(map(int, input().split())) for _ in range(int(input()))]
[print(*p) for p in sorted(pos, key=lambda x: (x[1], x[0]))]