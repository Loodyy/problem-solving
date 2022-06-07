def solve(a, b):
    result = 0

    a -= a * b/100
    if a < 100: result = 1 

    return result

def main():

    a, b = map(int, input().split())
    print(solve(a, b))

if __name__ == "__main__":

    main()
