#!/usr/bin/node
/* A script that sends a get request to a url */
const url = process.argv.slice(2);
fetch(url).then(response => {
  console.log(response.status);
});
