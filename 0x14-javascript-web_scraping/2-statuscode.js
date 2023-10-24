#!/usr/bin/node
/* A script that sends a get request to a url */
const request = require('request');
const url = process.argv.slice(2);
request(url[0], (error, response, body) => {
  if (error) {
    return;
  }
  console.log('code: ' + response.statusCode);
});
