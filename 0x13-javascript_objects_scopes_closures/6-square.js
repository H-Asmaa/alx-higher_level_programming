#!/usr/bin/node

const Square_ = require('./5-square.js');

class Square extends Square_ {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c = 'X') {
    let row = '';
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        row += c;
      }
      console.log(row);
      row = '';
    }
  }
}
module.exports = Square;
