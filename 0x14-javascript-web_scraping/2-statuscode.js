#!/usr/bin/node

// A script that display the status code of a GET
const request = require('request');
request.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
