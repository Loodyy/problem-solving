def solve(sub, x, y, n):
    pivot = sub[y][x]

    if n == 1:
        cnt[pivot+1] += 1
        return

    for i in range(n):
        for j in range(n):
            if sub[y+i][x+j] != pivot:
                for p in range(0, n, n//3):
                    for q in range(0, n, n//3):
                        solve(sub, x+p, y+q, n//3)
                return
    cnt[pivot+1] += 1 

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
cnt = [0] * 3
solve(paper, 0, 0, n)

[print(c) for c in cnt]