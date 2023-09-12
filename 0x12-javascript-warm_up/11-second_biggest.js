#!/usr/bin/node
function secondBiggest (list) {
  let first = -1;
  let second = -1;
  for (const i of list) {
    if (first < i) {
      second = first;
      first = i;
    } else if (second < i && first > i) {
      second = i;
    }
  }
  return second;
}
const args = process.argv.slice(2);
let res = 0;
if (!args[0]) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  res = secondBiggest(args);
  console.log(res);
}
