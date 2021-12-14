#!/usr/bin/node
const preSquare = require('./5-square');

class Square extends preSquare {
}

Square.prototype.charPrint = function (c) {
  if (!c) {
    c = 'X';
  }
  for (let i = 0; i < this.width; i++) {
    console.log(c.repeat(this.width));
  }
};

module.exports = Square;
