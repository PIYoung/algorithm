const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  console.log(
    input
      .filter((e, i) => i !== 0)
      .map((e, i) => e.split(" "))
      .sort((a, b) => Number(a[0]) - Number(b[0]))
      .join("\n")
      .replace(/,/g, " ")
  );

  process.exit();
});
