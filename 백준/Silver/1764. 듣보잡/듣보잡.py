n, m = map(int, input().split())
notListen = set([input() for _ in range(n)])
notSeen = set([input() for _ in range(m)])

notLS = sorted(list(notListen&notSeen))
print(len(notLS))
[print(ls) for ls in notLS]