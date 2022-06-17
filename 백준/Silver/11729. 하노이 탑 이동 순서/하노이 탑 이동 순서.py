def solve(n, s, e):
    if n == 1:
        ctrl.append([s, e])
        return

    solve(n-1, s, 6-s-e)
    ctrl.append([s, e])
    solve(n-1, 6-s-e, e)
    return

def main():

    n = int(input())
    solve(n, 1, 3) # 1 -> 3
    print(len(ctrl))
    for c in ctrl:
        print(*c)

if __name__ == "__main__":
    ctrl = []
    main()