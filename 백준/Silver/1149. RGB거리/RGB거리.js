const fs = require("fs");

const main = () => {
  const input = fs.readFileSync("/dev/stdin", "utf-8").trim().split("\n");
  const n = input[0];
  const paints = [];
  input.slice(1).forEach((str) => {
    paints.push(str.split(" ").map((x) => +x));
  });
  const minValue = solve(n, paints);
  console.log(minValue);
};

const solve = (n, paints) => {
  paints.forEach((_, i) => {
    if (i == 0) return;
    const prev = paints[i - 1];
    const curr = paints[i];
    curr.forEach((x, j) => {
      const prevMin = Math.min(...prev.filter((_, i) => i != j));
      curr[j] = x + prevMin;
    });
  });

  return Math.min(...paints.at(-1));
};

main();
