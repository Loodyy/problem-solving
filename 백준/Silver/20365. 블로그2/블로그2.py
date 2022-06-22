n = int(input())
string = input()

dic = {"B": 0, "R": 0}
comp = string[0]
dic[comp] += 1
for i in range(1, n):
    now = string[i]
    if comp != now:
        dic[now] += 1
        comp = now

print(min(dic["B"], dic["R"])+1)