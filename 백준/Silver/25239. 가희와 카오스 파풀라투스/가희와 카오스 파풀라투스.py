def solve():
    for x in query:
        t, i = x.split()
        if int(t.split(".")[0]) >= 60: break
        if i == "^":
            conq(h)
        else:
            if i[-1] == "N":
                dm = i[:len(i)-3]
                calc_time(0, int(dm))
            else:
                dh = i[:len(i)-4]
                calc_time(int(dh), 0)

    heal = sum(arr) - result if sum(arr)-result < 100 else 100 
    print(heal)
    return heal

def calc_time(dh, dm):
    global h, m

    h, m = h+dh, m+dm
    if m >= 60:
        m -= 60
        h += 1
    if h >= 12:
        h -= 12

def conq(h):
    global result

    if 0 <= h < 2: 
        if not dic["1"]:
            dic["1"] = True
            result += arr[0]
    elif 2 <= h < 4: 
        if not dic["2"]:
            dic["2"] = True
            result += arr[1]
    elif 4 <= h < 6: 
        if not dic["3"]:
            dic["3"] = True
            result += arr[2]
    elif 6 <= h < 8: 
        if not dic["4"]:
            dic["4"] = True
            result += arr[3]
    elif 8 <= h < 10: 
        if not dic["5"]:
            dic["5"] = True
            result += arr[4]
    elif 10 <= h < 12: 
        if not dic["6"]:
            dic["6"] = True
            result += arr[5]

h, m = map(int, input().split(":"))
arr = list(map(int, input().split()))
k = int(input())
query = [input() for _ in range(k)]
dic = {}
result = 0
for i in range(1, 7):
    dic[str(i)] = False

solve()