#!/usr/bin/node

const first = parseInt(process.argv[2]);
const second = parseInt(process.argv[3]);

function add (a, b) {
  const result = first + second;
  console.log(result);
}

add(first, second);
