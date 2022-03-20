s = input()
t = input()

def aa(arr):
    arr = arr[:len(arr)-1]
    return arr

def bb(arr):
    arr = arr[:len(arr)-1]
    arr = arr[::-1]
    return arr

result = 0
while len(s) != len(t):
    if t[len(t)-1] == "A":
        t = aa(t)
    else:
        t = bb(t)
    if s == t:
        result = 1

print(result) 