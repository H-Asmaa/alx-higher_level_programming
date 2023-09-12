#!/usr/bin/node
function factorial (n) {
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}
const args = process.argv.slice(2);
let res = 0;
if (!args[0]) {
  res = 1;
  console.log(res);
} else if (!isNaN(args[0])) {
  res = factorial(parseInt(args[0]));
  console.log(res);
}
