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
    [...new Set(input.filter((e, i) => i !== 0))]
      .sort((a, b) => {
        if (a.length === b.length) {
          return a > b ? 1 : -1;
        } else {
          return a.length - b.length;
        }
      })
      .join("\n")
  );

  process.exit();
});
