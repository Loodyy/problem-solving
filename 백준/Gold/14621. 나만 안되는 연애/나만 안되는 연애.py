def solve(sexarr, edges, parent):

    result = 0

    candi = []
    for a, b, cost in edges:
        if sexarr[a-1] == sexarr[b-1]:
            continue
        candi.append((cost, a, b))
    candi.sort()

    edge_cnt = 0
    for cost, a, b in candi:
        a, b = find_parent(a, parent), find_parent(b, parent)
        if a == b:
            continue
        else:
            union_parent(a, b, parent)
            result += cost
            edge_cnt += 1

    if edge_cnt < len(sexarr)-1: result = -1

    return result

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union_parent(a, b, parent):
    a, b = find_parent(a, parent), find_parent(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def main():

    n, m = map(int, input().split())
    sexarr = input().split()
    edges = [list(map(int, input().split())) for _ in range(m)]
    parent = list(range(n+1))
    print(solve(sexarr, edges, parent))

if __name__ == "__main__":

    main()
