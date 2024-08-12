#!/usr/bin/node

const request = require('request');
const argv = process.argv.slice(2);

request.get(
  `https://swapi-api.alx-tools.com/api/films/${argv[0]}`,
  (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    console.log(JSON.parse(body).title);
  }
);
