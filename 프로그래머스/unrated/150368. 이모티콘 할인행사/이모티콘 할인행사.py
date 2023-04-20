import itertools

def solution(users, emoticons):
    answer = []
    discountList = [0, 10, 20, 30, 40]
    
    emoticonList = []
    for discount in itertools.product(discountList, repeat=len(emoticons)):
        temp = []
        for price, rate in zip(emoticons, discount):
            temp.append((price * (100 - rate) // 100, rate))
        emoticonList.append(temp)
    
    maxPlus = maxIncome = 0
    for emoticonSet in emoticonList:
        tempPlus = tempIncome = 0
        for user in users:
            info = getUserBuyInfo(user, emoticonSet)
            tempPlus += int(info[0])
            tempIncome += info[1]
        
        if tempPlus > maxPlus or (tempPlus == maxPlus and tempIncome > maxIncome):
            maxPlus, maxIncome = tempPlus, tempIncome
        
    return [maxPlus, maxIncome]

def getUserBuyInfo(user, emoticonSet):
    isPlus = False
    
    wishDisRate = user[0]
    maxPay = user[1]
    pay = 0
    for ePrice, eDisRate in emoticonSet:
        if eDisRate >= wishDisRate:
            pay += ePrice
        
    if pay >= maxPay:
        pay = 0
        isPlus = True
        
    return isPlus, pay