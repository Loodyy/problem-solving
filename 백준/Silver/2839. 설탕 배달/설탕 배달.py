def solve(n):
    result = 0
    
    tmp = n
    cnt, tar = 0, 0
    while tmp >= 0:
        if tmp%3 == 0:
            tar = cnt
        cnt += 1
        tmp -= 5

    rest = n - tar*5
    if rest%3 == 0:
        result = tar + rest//3
    else:
        result = -1

    return result  

def main():

    n = int(input())
    print(solve(n))

if __name__ == "__main__":

    main()
