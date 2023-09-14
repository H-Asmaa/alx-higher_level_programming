#!/usr/bin/node
const list = require('./100-data.js').list;
let elem = 0;
const map_ = list.map((x) => x * elem++);
console.log(list);
console.log(map_);
