n = int(input())
words = [input() for _ in range(n)]

res = 0
for word in words:
    duple_check = True
    char_set = set(word[0])
    last_char = word[0]
    for w in word:
        if w != last_char:
            if w in char_set:
                duple_check = False
                break
            char_set.add(w)
            last_char = w
    if duple_check == True:
        res += 1

print(res)