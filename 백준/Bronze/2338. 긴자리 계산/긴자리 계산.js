let input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(BigInt);

let a = input[0];
let b = input[1];
console.log(`${a + b}\n${a - b}\n${a * b}`);