#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    let letter = c;
    if (!c) {
      letter = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let printLetter = '';
      for (let j = 0; j < this.height; j++) {
        printLetter += letter;
      }
      console.log(printLetter);
    }
  }
}

module.exports = Square;
