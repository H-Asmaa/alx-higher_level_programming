#!/usr/bin/node
/* A script that calculates the tasks completed for each user. */
const url = process.argv.slice(2)[0];
const request = require('request');
request(url, (error, response, body) => {
  if (error) { return; }
  let id = null; let counter = 0;
  const map = new Map();
  const data = JSON.parse(body);
  if (!data || !data.length) console.log(map);
  for (const dict of data) {
    if (dict.userId !== id) {
      if (counter > 0) map.set(id, counter);
      id = dict.userId;
      counter = 0;
    }
    if (dict.completed) counter++;
  }
  if (counter !== 0) map.set(id, counter);
  console.log(map);
});
