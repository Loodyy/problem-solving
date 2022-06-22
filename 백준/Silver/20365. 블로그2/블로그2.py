n = int(input())
string = input()
comp = string[0]
dic = {"B": 0, "R": 0}
dic[comp] += 1
for i in range(1, n):
    now = string[i]
    if comp != now:
        dic[now] += 1
        comp = now

if dic["B"] > dic["R"]:
    res = 1+dic["R"]
else:
    res = 1+dic["B"]

print(res)