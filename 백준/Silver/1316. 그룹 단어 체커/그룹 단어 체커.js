const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  const count = Number(input[0]);
  let answer = count;

  loop1:
  for (let i = 1; i <= count; i++) {
    const word = input[i];
    for (let j = 0; j < word.length; j++) {
      let checkStart = false;
      const str1 = word[j];
      for (let k = j + 1; k < word.length; k++) {
        const str2 = word[k];
        if (str1 !== str2) checkStart = true;
        if (checkStart && str1 === str2) {
          answer--;
          continue loop1;
        }
      }
    }
  }

console.log(answer);

  process.exit();
});