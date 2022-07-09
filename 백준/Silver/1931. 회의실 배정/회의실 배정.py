import sys
input = sys.stdin.readline

def select(start, i):
    for idx in range(i, len(meet)):
        m = meet[idx]
        if m[0] < start:
            continue
        return idx
    return -1

n = int(input())
meet = [list(map(int, input().split())) for _ in range(n)]
meet.sort(key=lambda x: (x[1], x[0]))

cnt, idx, start = 0, -1, 0
while True:
    idx = select(start, idx+1)
    if idx == -1:
        break
    start = meet[idx][1]
    cnt += 1

print(cnt)