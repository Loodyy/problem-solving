num = int(input())
arr = []
for _ in range(num):
    temp = list(map(int, input().split()))
    arr.append(temp)

# temp : 0 = x1, 1 = y1, 3 = x2, 4 = y2 
def solve():
    for i in range(num):
        temp = arr[i]
        dist = ((temp[3] - temp[0])**2 + (temp[4] - temp[1])**2)**(1/2)
        big = max(temp[2], temp[5])
        small = min(temp[2], temp[5])
        if temp[0] == temp[3] and temp[1] == temp[4]:
            if temp[2] == temp[5]:
                print(-1)
            else:
                print(0)
        else:
            if dist == temp[2] + temp[5] or dist == big - small:
                print(1)
            elif dist > temp[2] + temp[5] or big > dist + small :
                print(0)
            else:
                print(2)

solve()
