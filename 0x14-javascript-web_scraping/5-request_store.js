#!/usr/bin/node
/* A script that gets the contents of a webpage and stores
it in a file. */
const url = process.argv.slice(2)[0];
const path = process.argv.slice(2)[1];
const request = require('request');
const fs = require('fs');
request(url, (error, response, body) => {
  if (error) {
    return;
  }
  const data = body;
  fs.writeFile(path, data, (err) => {
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
});
