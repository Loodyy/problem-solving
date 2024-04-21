N, M = map(int, input().split())
ans = []

def bfs(curr, used):
    if len(curr) == M:
        ans.append(" ".join(map(str, curr)))
        return
    
    for i in range(1, N+1):
        if used[i]:
            continue

        used[i] = True
        curr.append(i)
        bfs(curr, used)
        curr.pop()
        used[i] = False

bfs([], [False] * (N+1))
print("\n".join(ans))