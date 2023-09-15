#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);
if (args.length === 3) {
  const fileA = args[0];
  const fileB = args[1];
  const fileC = args[2];
  let concate = '';
  fs.readFile(fileA, 'utf-8', (err, data) => {
    if (err) {
      console.error('Error Reading from ' + fileA + ' : ' + err);
      return;
    }
    concate += data;
    fs.readFile(fileB, 'utf-8', (err, data) => {
      if (err) {
        console.error('Error Reading from ' + fileB + ' : ' + err);
        return;
      }
      concate += data;
      fs.writeFile(fileC, concate, 'utf-8', (err) => {
        if (err) {
          console.error('Erro writing to ' + fileC + ' : ' + err);
        }
      });
    });
  });
} else {
  console.error('REQUIRED : files to concatenate and output file.');
}
