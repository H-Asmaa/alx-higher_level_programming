#!/usr/bin/node
const fs = require('fs');
const file = process.argv.slice(2);
fs.readFile(file[0], 'utf-8', (err, data) => {
  if (err) {
    const error = {
      Error: err,
      errno: err.errno,
      code: err.code,
      syscall: err.syscall,
      path: err.path
    };
    console.error(error);
    return;
  }
  console.log(data);
});
