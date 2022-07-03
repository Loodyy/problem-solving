res = ""
arr = list(map(int, input().split()))
if sorted(arr) == arr:
    res = "ascending"
elif sorted(arr, reverse=True) == arr:
    res = "descending"
else:
    res = "mixed"
print(res)