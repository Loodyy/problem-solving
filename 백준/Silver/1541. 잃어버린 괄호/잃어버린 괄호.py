def solve(oper):
    global operlist

    while oper in operlist:
        idx = operlist.index(oper)
        if oper == "-":
            operlist[idx+1] *= -1
        operlist[idx-1] += operlist[idx+1]
        del operlist[idx:idx+2]

INF = int(1e9)
minV = INF
oper = input()
operlist = []

temp = ""
for char in oper:
    if char in {"+", "-"}:
        operlist.extend([int(temp), char])
        temp = ""
    else:
        temp += char
operlist.append(int(temp))

solve("+")
solve("-")
print(operlist[0])