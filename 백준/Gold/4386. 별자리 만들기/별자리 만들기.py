def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a, b = find_parent(a), find_parent(b)
    if a < b: parent[b] = a
    else: parent[a] = b

def solve():
    result = 0

    for edge in arr:
        cost, a, b = edge
        if find_parent(a) != find_parent(b):
            result += cost
            union_parent(a, b)

    result = round(result, 2)

    print(result)
    return

if __name__ == "__main__":

    n = int(input())
    stars = [0]
    for i in range(n):
        temp = list(map(float, input().split()))
        stars.append([temp[0], temp[1]])
    
    arr = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            a, b = stars[i], stars[j]
            cost = ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)
            arr.append([cost, i, j])
    
    arr.sort()

    parent = list(range(n+1))

    solve()

