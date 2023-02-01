n, m = int(input()), int(input())

targ = input()
comp = "I" + "OI"*n

cnt = 0
for i in range(m):
    if comp == targ[i:i+len(comp)]:
        cnt += 1

print(cnt)