#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  if (body) {
    const obj = JSON.parse(body);
    const character = 'https://swapi-api.alx-tools.com/api/people/18/';
    const newArr = obj.results.filter((value) => {
      return value.characters.includes(character);
    });
    console.log(newArr.length);
  }
});
