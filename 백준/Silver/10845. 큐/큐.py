import sys
input = sys.stdin.readline

K = int(input())

que = []
for _ in range(K):
    cmd = input().split()
    if len(cmd) == 2:
        que.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if que:
            print(que.pop(0))
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(que))
    elif cmd[0] == "empty":
        if que:
            print(0)
        else:
            print(1)
    elif cmd[0] == "front":
        if que:
            print(que[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if que:
            print(que[-1])
        else:
            print(-1)