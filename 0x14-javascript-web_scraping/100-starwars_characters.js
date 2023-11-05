#!/usr/bin/node
/* A script that prints all characters of a Star Wars movie. */
const request = require('request');
const movieId = process.argv.slice(2)[0];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
request(url, (error, response, body) => {
  if (error) { return; }
  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    request(character, (error, response, body) => {
      if (error) { return; }
      console.log(JSON.parse(body).name);
    });
  }
});
