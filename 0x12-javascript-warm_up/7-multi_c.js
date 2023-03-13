#!/bin/node

const xTimes = parseInt(process.argv[2]);

if (Number.isInteger(xTimes)) {
  for (let i = 0; i < xTimes; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
