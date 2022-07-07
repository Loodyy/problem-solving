import sys
sys.setrecursionlimit(int(1e5))

def dfs(now, cnt):
    global res
    if cnt >= res:
        return

    if now == 1:
        res = min(res, cnt)
        return
    
    if now%3 == 0:
        dfs(now//3, cnt+1)
    if now%2 == 0:
        dfs(now//2, cnt+1)
    dfs(now-1, cnt+1)
 
res = int(1e9)
tar = int(input())
dfs(tar, 0)

print(res)