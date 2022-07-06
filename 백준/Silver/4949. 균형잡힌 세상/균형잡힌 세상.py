def solve(string):
    st = []
    for char in string:
        if char in "{([":
            st.append(char)
        elif char in "})]":
            if len(st) == 0:
                return False
            if st[-1] == "(" and char != ")":
                return False
            if st[-1] == "{" and char != "}":
                return False
            if st[-1] == "[" and char != "]":
                return False
            st.pop()
    
    if len(st) == 0:
        return True

while True:
    string = input()
    if string == ".":
        break
    if solve(string):
        print("yes")
    else:
        print("no")