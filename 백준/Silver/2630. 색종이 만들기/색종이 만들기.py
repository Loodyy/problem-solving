N = int(input())
PAPER = [list(map(int, input().split())) for _ in range(N)]

answer = [0] * 2
def cut_paper(x, y, n):
    global answer
    color = PAPER[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != PAPER[i][j]:
                cut_paper(x, y, n // 2)
                cut_paper(x, y + n // 2, n // 2)
                cut_paper(x + n // 2, y, n // 2)
                cut_paper(x + n // 2, y + n // 2, n // 2)
                return
    answer[color] += 1

cut_paper(0, 0, N)
print(*answer, sep='\n')