h, w = map(int, input().split())
walls = list(map(int, input().split()))

answer = 0

for i in range(1, len(walls)-1):
    l_h = max(walls[:i])
    r_h = max(walls[i+1:])

    comp = min(l_h, r_h)

    if walls[i] < comp:
        answer += comp - walls[i]

print(answer)