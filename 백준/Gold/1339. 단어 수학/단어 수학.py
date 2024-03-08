n = int(input())
words = []

alpha_cnt = dict()
for _ in range(n):
    word = list(input())
    words.append(word)
    for i, w in enumerate(word):
        if w not in alpha_cnt:
            alpha_cnt[w] = 0
        alpha_cnt[w] += 10 ** (len(word) - i - 1)

temp = list(alpha_cnt.items())
temp.sort(key=lambda x: x[1], reverse=True)

sub_dict = dict()
subed_num = 9
for k, _ in temp:
    sub_dict[k] = subed_num
    subed_num -= 1

answer = 0
for word in words:
    answer += int(''.join([str(sub_dict[w]) for w in word]))

print(answer)

