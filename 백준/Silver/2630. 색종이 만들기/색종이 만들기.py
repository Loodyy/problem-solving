def solve(x, y, n, paper):
    pivot = paper[y][x]
    if n == 1:
        cnt[pivot] += 1
        return

    for i in range(n):
        for j in range(n):
            if paper[y+i][x+j] != pivot:
                
                for p in range(0, n, n//2):
                    for q in range(0, n, n//2):
                        solve(x+p, y+q, n//2, paper)
                return
                
    cnt[pivot] += 1

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
cnt = [0] * 2
solve(0, 0, n, paper)

[print(c) for c in cnt]