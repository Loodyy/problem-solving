import sys
input = sys.stdin.readline

n = int(input())
meet = [list(map(int, input().split())) for _ in range(n)]
meet.sort(key=lambda x: (x[1], x[0]))

cnt, start = 0, 0
for i in range(n):
    if start <= meet[i][0]:
        cnt += 1
        start = meet[i][1]

print(cnt)