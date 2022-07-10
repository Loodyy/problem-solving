n, m = int(input()), int(input())
targ = input()

res = cnt = idx = 0
while idx < m:
    if targ[idx:idx+3] == "IOI":
        idx += 2
        cnt += 1
        if cnt == n:
            res += 1
            cnt -= 1
    else:
        idx += 1
        cnt = 0

print(res)