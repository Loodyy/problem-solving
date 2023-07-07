function solution(s) {
    const numList = s.split(" ").map(i => +i);
    let minVal = Number.MAX_VALUE;
    let maxVal = -minVal;
    
    numList.forEach(num => {
        minVal = Math.min(minVal, num);
        maxVal = Math.max(maxVal, num);
    })
    
    return `${minVal} ${maxVal}`
}