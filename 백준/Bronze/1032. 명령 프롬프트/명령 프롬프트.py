N = int(input())
strings = [input() for _ in range(N)]

ans = ""
for i in range(len(strings[0])):
    s = strings[0]
    for string in strings:
        if s[i] != string[i]:
            ans += "?"
            break
    else:
        ans += s[i]

print(ans)