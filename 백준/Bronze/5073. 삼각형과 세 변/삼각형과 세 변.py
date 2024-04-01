while True:
    arr = list(map(int, input().split()))
    if arr[0] == arr[1] == arr[2] == 0:
        break

    arr.sort()
    a, b, c = arr

    if c >= a + b:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")