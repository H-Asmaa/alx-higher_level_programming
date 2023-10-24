#!/usr/bin/node
/*A script that calculates the number of occurences
of the character Wedge Antilles that has the ID 8.*/
const request = require('request');
const url = process.argv.slice(2);
let counter = 0;
let result;
const target = 'https://swapi-api.alx-tools.com/api/people/18/';
request(url[0], (error, response, body) => {
  if (error) { return; }
  for (result of JSON.parse(body).results) {
    if (result.characters.includes(target)) { counter += 1; }
  }
  console.log(counter);
});
