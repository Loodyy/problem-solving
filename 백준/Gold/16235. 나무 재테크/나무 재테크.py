def solve(target):
    year = 0

    while True:

        if year == target:
            tree_num = 0
            for i in tree:
                for j in i:
                    for x in j:
                        if x > 0:
                            tree_num += 1
            print(tree_num)
            return
        
        temp = []
        for i in range(n):
            for j in range(n):
                now = tree[i][j]
                death = 0
                for k in range(len(now)-1, 0, -1):
                    if ground[i][j] >= now[k]:
                        ground[i][j] -= now[k]
                        now[k] += 1 # spring
                        if not now[k]%5:
                            temp.append([i, j])
                    else:
                        death += int(now[k]/2) 
                        now.pop(k)
                ground[i][j] += death # summer
            
        for tmp in temp:
            i, j = tmp
            for d in dir:
                dx, dy = d[0], d[1]
                if 0 <= j+dx < n and 0 <= i+dy < n:
                    tree[i+dy][j+dx].append(1) # fall
        
        for i in range(n):
            for j in range(n):
                ground[i][j] += arr[i][j] # winter

        year += 1

if __name__ == "__main__":
    n, m, target = map(int, input().split())
    ground = [[5]*n for _ in range(n)]
    arr = [list(map(int, input().split())) for _ in range(n)]
    tree = [[[0] for _ in range(n)] for _ in range(n)]
   
    for _ in range(m):
        a, b, age = map(int, input().split())
        tree[a-1][b-1].append(age)

    dir = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

    solve(target)