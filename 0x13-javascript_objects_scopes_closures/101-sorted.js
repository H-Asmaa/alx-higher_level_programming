#!/usr/bin/node

const dict = require('./101-data.js').dict;
const occDict = {};
let list = [];
for (const key in dict) {
  for (const key_ in dict) {
    if (dict[key] === dict[key_]) {
      list.push(key_);
    }
  }
  occDict[dict[key]] = list;
  list = [];
}
console.log(occDict);
