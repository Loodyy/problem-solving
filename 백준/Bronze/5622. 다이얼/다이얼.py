word = input()
match = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

res = 0
for chr in word:
    for i, tar in enumerate(match):
        if chr in tar:
            res += i+3

print(res)