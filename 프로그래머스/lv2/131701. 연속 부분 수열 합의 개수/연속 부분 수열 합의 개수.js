function solution(elements) {
    const sumSet = new Set();
    const maxLen = elements.length;
    
    for (let i = 1; i < maxLen + 1; i++) {
        for (let j = 0; j < maxLen; j++) {
            let sum = 0;
            for (let idx = j; idx < j + i; idx++) {
                sum += elements[idx % maxLen];
            }
            sumSet.add(sum);
        }
    }
    return sumSet.size;
}