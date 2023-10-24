#!/usr/bin/node
/* A script that sends a request to a URL with an id */
const request = require('request');
const id = process.argv.slice(2);
const url = 'https://swapi-api.alx-tools.com/api/films/' + id[0];
request(url, (error, response, body) => {
  if (error) {
    return;
  }
  console.log(JSON.parse(body).title);
});
