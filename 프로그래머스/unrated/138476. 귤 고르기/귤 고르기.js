function solution(k, tangerine) {
    const sizeCountMap = new Map();
    
    tangerine.forEach(size => {
        const count = sizeCountMap.get(size) ?? 0;
        sizeCountMap.set(size, count + 1);
    })
    
    const countList = Array.from(sizeCountMap.values()).sort((a, b) => b - a);
    let limit = k;
    const maxLen = countList.length;
    for (let i = 0; i < maxLen; i++) {
        limit -= countList[i];
        if (limit <= 0) {
            return i + 1;
        }
    }
    return maxLen;
}