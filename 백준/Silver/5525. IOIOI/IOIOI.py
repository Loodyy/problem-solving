def main():
    n = int(input())
    maxLen = int(input())
    target = input()
    cnt = solve(n, maxLen, target)
    print(cnt)

def solve(n, maxLen, target) -> int:
    cnt = 0
    comp: str = "I" + "OI" * n
    for i in range(maxLen):
        if i + len(comp) > maxLen:
            break
            
        isMatch = True
        for j, x in enumerate(comp):                
            if i + j < maxLen and x != target[i + j]:
                isMatch = False
                break

        cnt += bool(isMatch)
            
    return cnt

main() 