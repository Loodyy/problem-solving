A = list(input().replace("()", "|"))

ans = 0
S = []
for c in A:
    if c == "|":
        ans += len(S)
    elif c == "(":
        S.append(c)
    else:
        S.pop()
        ans += 1

print(ans)