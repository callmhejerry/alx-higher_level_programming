#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

function callback (error, response, body) {
  if (response) {
    console.log(`code: ${response.statusCode}`);
  }
}
request.get(url, callback);
