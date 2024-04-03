import sys
input = sys.stdin.readline 

N = int(input())
edges = [tuple(map(int, input().split())) for _ in range(N)]

answer = edges[N-1][0] * edges[0][1] - edges[N-1][1] * edges[0][0]
for i in range(N-1):
    answer += edges[i][0] * edges[i+1][1]
    answer -= edges[i][1] * edges[i+1][0]
answer = abs(round(answer/2, 1))

print(answer)