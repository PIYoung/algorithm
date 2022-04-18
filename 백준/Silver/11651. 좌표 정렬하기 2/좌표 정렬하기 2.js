const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  const coordinates = input
    .filter((e, i) => i !== 0)
    .map((e) => e.split(" ").map(Number))
    .sort((a, b) => {
      if (a[1] === b[1]) {
        return a[0] - b[0];
      } else {
        return a[1] - b[1];
      }
    })
    .join("\n")
    .replace(/,/g, " ");

  console.log(coordinates);

  process.exit();
});
