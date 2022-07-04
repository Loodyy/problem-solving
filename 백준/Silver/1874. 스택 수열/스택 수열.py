def solve():
    cnt, tidx, now = 0, 0, 1
    
    while cnt < n*2:
        tar = arr[tidx]
        if st and st[-1] == tar:
            st.pop()
            tidx += 1
            cnt += 1
            res.append("-")
            continue
        st.append(now)
        now += 1
        cnt += 1
        res.append("+")

        if now > n+1:
            print("NO")
            return

    for elem in res:
        print(elem)

n = int(input())
arr = [int(input()) for _ in range(n)]
st, res = [], []

solve()
