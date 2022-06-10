def solve(a, b):
    A, B = a, b
    alist, blist = [a], [b]
    acnt = bcnt = 0
    aend = bend = False
    target = 0
    if a != b:
        while True:
            ta = tb = 0
            if a != 1:
                if not a%2: 
                    ta = a//2
                else: ta = a*3+1

            if b != 1:
                if not b%2:
                    tb = b//2
                else: tb = b*3+1

            if ta in blist:
                target = ta
                alist.append(ta)
                break

            if ta != 1:
                alist.append(ta)
                a = ta
            elif not aend:
                alist.append(1)
                a = ta = 1
                aend = True

            if tb in alist:
                target = tb
                blist.append(tb)
                break

            if tb != 1:
                blist.append(tb)
                b = tb
            elif not bend:
                blist.append(1)
                b = tb = 1
                bend = True     
                       
        acnt, bcnt = alist.index(target), blist.index(target)
    else: target = a

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
