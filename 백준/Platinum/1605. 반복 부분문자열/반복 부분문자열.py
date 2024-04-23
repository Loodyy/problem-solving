MOD = 100_000_007

def pow(a, b, mod):
    if b == 0:
        return 1
    x = pow(a, b//2, mod)
    if b % 2 == 0:
        return (x*x) % mod
    else:
        return (x*x*a) % mod

def is_conflict(N, S, l):
    hash_map = dict() # hash, index

    curr_hash = 0
    for i in range(N-l+1):
        if i == 0: # first hash
            for j in range(l):
                curr_hash = (curr_hash + ord(S[j]) * pow(31, l-j-1, MOD)) % MOD
        else:
            curr_hash = (31 * (curr_hash - ord(S[i-1]) * pow(31, l-1, MOD)) + ord(S[i+l-1])) % MOD
        
        idxs = hash_map.get(curr_hash)
        if idxs and len(idxs) > 0:
            for idx in idxs:
                is_match = True
                for j in range(l):
                    if S[idx+j] != S[i+j]:
                        is_match = False
                if is_match:
                    return True
        else:
            hash_map[curr_hash] = []
        
        hash_map[curr_hash].append(i)

    return False

def solve():
    N, S = int(input()), input()
    ans = 0

    l, r = 1, N
    while l <= r:
        length = (l+r) // 2

        if is_conflict(N, S, length):
            ans = max(ans, length)
            l = length + 1
        else:
            r = length - 1
    return ans

print(solve())