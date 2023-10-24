#!/usr/bin/node
const file = process.argv.slice(2);
const fs = require('fs');
fs.writeFile(file[0], file[1], 'utf-8', err => {
  if (err) {
    const error = {
      Error: err,
      errno: err.errno,
      code: err.code,
      syscall: err.syscall,
      path: err.path
    };
    console.log(error);
  }
});
