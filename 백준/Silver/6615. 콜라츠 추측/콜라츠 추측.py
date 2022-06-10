def solve(a, b):
    A, B = a, b

    adic = {}
    acnt = 1
    while a != 1:
        adic[a] = acnt
        if not a%2:
            a = a//2
        else: a = a*3+1
        acnt += 1
    adic[a] = acnt

    bcnt = 0
    while b != 1:

        if adic.get(b):
            acnt = adic[b]-1
            target = b
            print("{} needs {} steps, {} needs {} steps, they meet at {}".format(A, acnt, B, bcnt, target))
            return

        if not b%2:
            b = b//2
        else: b = b*3+1

        bcnt += 1

    acnt = adic[1]-1
    target = 1
    print("{} needs {} steps, {} needs {} steps, they meet at {}".format(A, acnt, B, bcnt, target))
    return

def main():

    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        solve(a, b)

if __name__ == "__main__":

    main()
