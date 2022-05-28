import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

def solve():

    occupy = [0] * (m+1)
    cnt = 0
    for i in range(1, n+1):
        visited = [False] * (m+1)
        if dfs(i, occupy, visited): 
            cnt += 1

    print(cnt)
    return

def dfs(x, occupy, visited):

    for tar in graph[x]:
        if visited[tar]: continue
        visited[tar] = True
        if not occupy[tar] or dfs(occupy[tar], occupy, visited):
            occupy[tar] = x
            return True
    return False

if __name__ == "__main__":

    k = int(input())
    for _ in range(k):
        n, m = map(int, input().split())
        graph = [[] for _ in range(n+1)]
        for i in range(1, m+1):
            a, b = map(int, input().split())
            for j in range(a, b+1): 
                graph[j].append(i)
        solve()
