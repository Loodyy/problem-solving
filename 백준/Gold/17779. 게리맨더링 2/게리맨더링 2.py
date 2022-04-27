def solve():
    result = []

    for y in range(n): # brute force
        for x in range(1, n):
            for d1 in range(1,n):
                for d2 in range(1, n): 
                    if y+d1+d2 < n and 0 <= x-d1 and x+d2 < n:
                        result.append(separate(x, y, d1, d2))
                        
    print(min(result))
    return

def separate(x, y, d1, d2):
    area = [[0] * n for _ in range(n)]
    people = [0] * 6

    # threshold
    for i in range(d1+1): 
        area[y+i][x-i] = 5
        area[y+d2+i][x+d2-i] = 5
    for j in range(d2+1):
        area[y+j][x+j] = 5
        area[y+d1+j][x-d1+j] = 5

    # inner
    for p in range(y+1, y+d1+d2):
        temp = []
        for q, a in enumerate(area[p]):
            if a == 5: temp.append(q)
        for q in range(temp[0], temp[1]):
            area[p][q] = 5

    # 1 ~ 4
    for i in range(y+d1):
        for j in range(x+1):
            if area[i][j] != 5: area[i][j] = 1
    for i in range(y+d2+1):
        for j in range(x+1, n):
            if area[i][j] != 5: area[i][j] = 2
    for i in range(y+d1, n):
        for j in range(x-d1+d2):
            if area[i][j] != 5: area[i][j] = 3
    for i in range(y+d2+1, n):
        for j in range(x-d1+d2, n):
            if area[i][j] != 5: area[i][j] = 4

    for i in range(n):
        for j in range(n):
            people[area[i][j]] += arr[i][j]
 
    diff = max(people) - min(people[1:])
    return diff

if __name__ == "__main__":

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    solve()
