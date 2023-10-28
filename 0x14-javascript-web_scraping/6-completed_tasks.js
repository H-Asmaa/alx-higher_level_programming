#!/usr/bin/node
/* A script that calculates the tasks completed for each user. */
const url = process.argv.slice(2)[0];
const request = require('request');
request(url, (error, response, body) => {
  if (error) { return; }
  const data = JSON.parse(body);
  let id = null; let counter;
  const usersTasks = {};
  if (!data || !data.length) {
    console.log(usersTasks);
    return;
  }
  for (const dict of data) {
    if (dict.userId !== id) {
      if (counter > 0) usersTasks[id] = counter;
      id = dict.userId;
      counter = 0;
    }
    if (dict.completed) counter++;
  }
  if (counter !== 0) usersTasks[id] = counter;
  console.log(usersTasks);
});
