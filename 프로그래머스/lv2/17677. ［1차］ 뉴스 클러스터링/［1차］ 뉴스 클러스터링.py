def solution(str1, str2):
    answer = 0
    
    
    list1, list2 = [], []
    len1, len2 = len(str1), len(str2)
    
    list1 = [str1[i:i+2].lower() for i in range(len1-1) if str1[i:i+2].isalpha()]
    list2 = [str2[j:j+2].lower() for j in range(len2-1) if str2[j:j+2].isalpha()]
    
#     for i in range(len1-1):
#         if str1[i].isalpha() and str1[i+1].isalpha():
#             key = str1[i].lower() + str1[i+1].lower()
#             list1.append(key)
    
#     for j in range(len2-1):
#         if str2[j].isalpha() and str2[j+1].isalpha():
#             key = str2[j].lower() + str2[j+1].lower()
#             list2.append(key)
    
    if len(list1) + len(list2) == 0:
        return 2**16

    print(list1, list2)
    
    unionn = len(list1) + len(list2) # temp
    
    intern = 0
    for x in list1:
        if x in list2:
            list2.remove(x)
            intern += 1
            
    unionn -= intern 

    jcard = intern / unionn
    
    answer = int(jcard * 2**16)

    return answer