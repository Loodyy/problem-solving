n = int(input())
cnt = [0] * 2 # 2, 5

for i in range(1, n+1):
    while i > 0:
        if i%2 == 0:
            cnt[0] += 1
            i //= 2
        elif i%5 == 0:
            cnt[1] += 1
            i //= 5
        else: break

print(min(cnt))