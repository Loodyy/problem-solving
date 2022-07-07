n = int(input())
oper = input()
nums = [int(input()) for _ in range(n)]

stack = []
for char in oper:
    if char.isalpha():
        stack.append(nums[ord(char) - ord('A')])
    else:
        if char == "+":
            stack.append(stack.pop() + stack.pop())
        elif char == "-":
            stack.append(-stack.pop() + stack.pop())
        elif char == "*":
            stack.append(stack.pop() * stack.pop())
        elif char == "/":
            sec, fir = stack.pop(), stack.pop()
            stack.append(fir / sec)

print("%.2f" % stack[0])