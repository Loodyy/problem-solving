TK = int(input())
for _ in range(TK):
    string = input()
    while "()" in string:
        string = string.replace("()", "")
        
    if string == "":
        print("YES")
    else:
        print("NO")