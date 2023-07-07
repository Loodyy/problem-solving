function solution(babbling) {
    const canWords = getCanWords(["aya", "ye", "woo", "ma"]);
    return babbling.filter(word => canWords.has(word)).length;
}

const getCanWords = (babbling) => {
    const cnts = Array(babbling.length).fill(1);
    const wordSet = new Set();
    setWords(babbling, cnts, wordSet, []);
    return wordSet;
}

const setWords = (babbling, cnts, set, curr) => {
    set.add(curr.map(idx => babbling[idx]).join(''))
    for (let i = 0; i < babbling.length; i++) {
        if (cnts[i] === 1) {
            cnts[i] -= 1;
            curr.push(i)
            setWords(babbling, cnts, set, curr);
            cnts[i] += 1;
            curr.pop();
        }
    }
}