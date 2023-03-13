#!/usr/bin/node

const square = Number(process.argv[2]);

if (Number.isInteger(square)) {
  for (let i = 0; i < square; i++) {
    let x = '';
    for (let j = 0; j < square; j++) {
      x += 'X';
    }
    console.log(x);
  }
} else {
  console.log('Missing size');
}
