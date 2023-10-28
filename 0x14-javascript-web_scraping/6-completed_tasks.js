#!/usr/bin/node
const url = process.argv.slice(2)[0];
const request = require('request');
request(url, (error, response, body) => {
  if (error) { return; }
  let id = JSON.parse(body)[0].userId; let counter = 0;
  const usersTasks = {};
  for (const dict of JSON.parse(body)) {
    if (dict.userId === id) {
      if (dict.completed === true) { counter++; }
    } else {
      if (counter > 0) {
        usersTasks[id] = counter;
        counter = 0;
      }
      if (dict.completed) counter++;
      id = dict.userId;
    }
  }
  if (counter !== 0) usersTasks[id] = counter;
  console.log(usersTasks);
});
