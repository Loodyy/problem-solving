n, k = map(int, input().split())

key_dic = {}
value_dic = {}
for i in range(n):
    tar = input()
    key_dic[tar] = i+1
    value_dic[i+1] = tar

for _ in range(k):
    cmd = input()
    if cmd.isdigit():
        print(value_dic[int(cmd)])
    else:
        print(key_dic[cmd])