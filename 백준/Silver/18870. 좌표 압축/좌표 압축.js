const fs = require("fs");
const file = "/dev/stdin";
// const file = `${__dirname}/dev/stdin.txt`;
const input = fs.readFileSync(file).toString().split("\n");

const numbers = input[1].split(" ").map(Number);
const obj = {};
const result = [];

[...new Set([...numbers].sort((a, b) => a - b))].forEach((e, i) => {
  obj[e] = i;
});

for (let i = 0; i < numbers.length; i++) {
  result.push(obj[numbers[i]]);
}

console.log(result.join(" "));
