#!/usr/bin/node
const args = process.argv.slice(2);
if (args[0] && args[1]) {
  console.log(args[0] + ' is ' + args[1]);
} else if (args[0]) {
  console.log(args[0] + ' is undefined');
} else {
  console.log('undefined is undefined');
}
