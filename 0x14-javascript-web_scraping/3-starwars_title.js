#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  if (body) {
    const obj = JSON.parse(body);
    console.log(obj.title);
  }
});
