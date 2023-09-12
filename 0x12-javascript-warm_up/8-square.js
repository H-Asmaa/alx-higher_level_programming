#!/usr/bin/node
const args = process.argv.slice(2);
let row = '';
if (!isNaN(args[0]) && args[0] >= 0) {
  for (let i = 0; i < args[0]; i++) {
    for (let j = 0; j < args[0]; j++) {
      row += 'X';
    }
    console.log(row);
    row = '';
  }
} else if (isNaN(args[0])) {
  console.log('Missing size');
}
