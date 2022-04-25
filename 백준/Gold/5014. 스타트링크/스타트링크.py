from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)

def solve(src):
    
    result = 0
    
    q = deque()
    visited = [False] * (f+1)

    q.append((src, 0))
    visited[src] = True

    while q:
        now, cnt = q.popleft()
        if now == dst:
            print(cnt)
            return 
        for i in range(2):
            th = now+u if i == 0 else now-d
            if 0 < th <= f and not visited[th]:
                visited[th] = True
                q.append((th, cnt+1))

    print("use the stairs")
    return 

if __name__ == "__main__":

    f, src, dst, u, d = map(int, input().split())
    visited = [False] * (f+1)
    visited[src] = True

    solve(src)

    
