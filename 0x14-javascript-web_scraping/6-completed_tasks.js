#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  if (response.statusCode === 200) {
    const obj = JSON.parse(body);
    const data = {};
    for (const todo of obj) {
      if (todo.userId in data) {
        if (todo.completed) {
          data[todo.userId] += 1;
        }
      } else {
        data[todo.userId] = 0;
        if (todo.completed) {
          data[todo.userId] += 1;
        }
      }
    }
    console.log(data);
  }
});
