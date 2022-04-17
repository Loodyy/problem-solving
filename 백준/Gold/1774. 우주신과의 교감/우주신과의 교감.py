def solve():
    result = 0
    
    for i in connected:
        union_parent(i[0], i[1])

    for i in temp:
        cost, a, b = i
        if find_parent(a) != find_parent(b):
            result += cost
            union_parent(a, b)

    print("%.2f" % result)
    return

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a, b = find_parent(a), find_parent(b)
    if a < b: parent[b] = a
    else: parent[a] = b

if __name__ == "__main__":

    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    temp = []
    for i in range(n):
        for j in range(i+1, n):
            fir, sec = arr[i], arr[j]
            dist = ((fir[0]-sec[0])**2 + (fir[1]-sec[1])**2)**(1/2)
            temp.append([dist, i+1, j+1])
    temp.sort()

    connected = []
    for i in range(m):
        connected.append(list(map(int, input().split())))
  
    parent = list(range(n+1))

    solve()