const input = require('fs').readFileSync('/dev/stdin').toString().split(' ');
const origin = [1, 1, 2, 2, 2, 8];
input.forEach((piece, idx) => {
  process.stdout.write(origin[idx] - piece + ' ');
});
