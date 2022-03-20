import itertools

n, m = map(int, input().split())
arr = []
h_list = []
c_list = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 1:
            h_list.append((i, j))
        if temp[j] == 2:
            c_list.append((i, j)) 
 
result_dist = []

ncr = list(itertools.combinations(c_list, m))
min_result = []
for x in ncr:
    temp_result = 0
    for y in h_list:
        temp_dist = n * n
        for z in x:
            temp = abs(y[0] - z[0]) + abs(y[1] - z[1])
            if temp_dist > temp:
                temp_dist = temp
        temp_result += temp_dist
    min_result.append(temp_result)

print(min(min_result))

            

