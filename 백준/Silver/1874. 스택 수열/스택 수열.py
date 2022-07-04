import sys
input = sys.stdin.readline

def solve():
    now = 1
    for _ in range(n):
        tar = int(input())
        while now <= tar:
            st.append(now)
            res.append("+")
            now += 1
        if st[-1] == tar:
            st.pop()
            res.append("-")
        else:
            print("NO")
            return 
    
    for elem in res:
        print(elem)

n = int(input())
st, res = [], []

solve()