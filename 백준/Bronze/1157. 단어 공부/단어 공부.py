string = input()
string = string.upper()

dic = {}
for s in string:
    if dic.get(s): dic[s] += 1
    else: dic[s] = 1

temp = list(dic.items())
temp.sort(key=lambda x: -x[1])

res = ""
if len(temp) > 1 and temp[0][1] == temp[1][1]:
    res = "?"
else: 
    res = temp[0][0]

print(res)