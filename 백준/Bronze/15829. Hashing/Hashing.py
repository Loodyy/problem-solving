n = int(input())
string = input()
res = 0
for i, x in enumerate(string):
    res += (ord(x)-96)*(31**i)
res %= 1234567891

print(res)