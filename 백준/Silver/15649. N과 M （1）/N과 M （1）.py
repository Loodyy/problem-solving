N, M = map(int, input().split())
ans = []

def bfs(curr, num_set: set):
    if len(curr) == M:
        ans.append(" ".join(map(str, curr)))
        return
    
    for i in range(1, N+1):
        if i in num_set:
            continue
        next_set = num_set.copy()
        next_set.add(i)
        curr.append(i)
        bfs(curr, next_set)
        curr.pop()

bfs([], set())
[print(a) for a in ans]