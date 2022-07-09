import sys
input = sys.stdin.readline

n = int(input())

res = set()
for _ in range(n):
    cmd = input().split()
    if len(cmd) > 1:
        cmd[1] = int(cmd[1])

    if cmd[0] == "add":
        res.add(cmd[1])
    elif cmd[0] == "remove":
        if cmd[1] in res:
            res.remove(cmd[1])
    elif cmd[0] == "check":
        if cmd[1] in res:
            print(1)
        else:
            print(0)
    elif cmd[0] == "toggle":
        if cmd[1] in res:
            res.remove(cmd[1])
        else:
            res.add(cmd[1])
    elif cmd[0] == "all":
        res.update(list(range(1, 21)))
    elif cmd[0] == "empty":
        res.clear()