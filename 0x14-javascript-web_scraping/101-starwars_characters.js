#!/usr/bin/node
const request = require('request');
const util = require('util');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, async (err, res, body) => {
  if (err) {
    console.log(err);
  }
  if (body) {
    const data = JSON.parse(body);
    const charactersUrl = data.characters;
    const promisedRequest = util.promisify(request.get);
    const writeFile = async (url) => {
      const res = await promisedRequest(url);
      const data = JSON.parse(res.body);
      console.log(data.name);
    };
    for (const character of charactersUrl) {
      await writeFile(character);
    }
  }
});
