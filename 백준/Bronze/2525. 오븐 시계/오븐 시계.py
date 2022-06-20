y, m = map(int, input().split())
required = int(input())

total = y*60 + m +required

resy = total//60
resm = total%60 
if resy >= 24:
    resy -= 24

print(*(resy, resm))