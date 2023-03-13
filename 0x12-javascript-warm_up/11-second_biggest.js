#!/bin/node

const argv = process.argv;

if (argv.length <= 3) {
  console.log(0);
} else {
  const numbers = [];

  for (let i = 2; i < argv.length; i++) {
    numbers.push(parseInt(argv[i]));
  }

  numbers.sort((a, b) => b - a);
  console.log(numbers[1]);
}
