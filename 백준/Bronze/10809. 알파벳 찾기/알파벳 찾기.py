string = input()
cnt = [-1] * 26
for i, s in enumerate(string):
    alpha_idx = ord(s)-97
    if cnt[alpha_idx] > -1:
        continue
    cnt[alpha_idx] = i
print(*cnt)