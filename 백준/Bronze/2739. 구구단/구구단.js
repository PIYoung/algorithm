const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", function (line) {
  const input = line;

  const num = Number(input);

  for (let i = 1; i <= 9; i++) {
      console.log(`${num} * ${i} = ${num * i}`);
  }

  rl.close();
}).on("close", function () {
  process.exit();
});