S, T = input(), input()
can_covt = False

def covt_a(T):
    return T[:-1]

def covt_b(T):
    return T[1:][::-1]

def solve(S, T):
    global can_covt

    if len(S) >= len(T):
        if S == T:
            can_covt = True
        return
    
    if T[-1] == "A":
        solve(S, covt_a(T))
    if T[0] == "B":
        solve(S, covt_b(T))

solve(S, T)
print(int(can_covt))