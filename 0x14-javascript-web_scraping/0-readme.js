#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];

function callBack (data, err) {
  if (data) {
    console.log(data);
  } else {
    console.log(err);
  }
}
fs.readFile(filePath, { encoding: 'utf-8' }, callBack);
