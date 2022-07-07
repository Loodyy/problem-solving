def checking(x, y, n):
    global cnt
    if c < x or x+n < c or r < y or y+n < r:
        cnt += n**2
        return

    if n == 2:
        for i in range(2):
            for j in range(2):
                if (x+j, y+i) == (c, r):
                    print(cnt)
                cnt += 1
        return

    checking(x, y, n//2)
    checking(x+n//2, y, n//2)
    checking(x, y+n//2, n//2)
    checking(x+n//2, y+n//2, n//2)

n, r, c = map(int, input().split())
cnt = 0

checking(0, 0, 2**n)