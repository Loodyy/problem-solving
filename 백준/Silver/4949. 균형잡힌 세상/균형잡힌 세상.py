def solve(string):
    temp = ""
    for char in string:
        if char in "{}()[]":
            temp += char
    
    while "{}" in temp or "[]" in temp or "()" in temp:
        temp = temp.replace("{}", "")
        temp = temp.replace("[]", "")
        temp = temp.replace("()", "")
    
    if temp == "":
        print("yes")
    else:
        print("no")

while True:
    string = input()
    if string == ".":
        break
    solve(string)