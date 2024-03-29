#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  if (body) {
    const data = JSON.parse(body);
    const charactersUrl = data.characters;

    for (const character of charactersUrl) {
      request.get(character, (err, res, body) => {
        if (err) {
          console.log(err);
        }
        if (res.statusCode === 200) {
          const actor = JSON.parse(body);
          console.log(actor.name);
        }
      });
    }
  }
});
