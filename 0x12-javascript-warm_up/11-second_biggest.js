#!/usr/bin/node
function secondBiggest (list) {
  let first = -Infinity;
  let second = -Infinity;
  for (const i of list) {
    if (!isNaN(Number(i))) {
      if (first < Number(i)) {
        second = first;
        first = Number(i);
      } else if (second < Number(i) && first !== Number(i)) {
        second = Number(i);
      }
    }
  }
  return second;
}
const args = process.argv.slice(2);
if (!args[0] || args.length === 1) {
  console.log(0);
} else {
  console.log(secondBiggest(args));
}
