#!/usr/bin/node

const list = require('./100-data.js').list;

const newList = list.map((element, idx) => {
  return element * idx;
});

console.log(list);
console.log(newList);
