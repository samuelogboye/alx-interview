#!/usr/bin/node

const request = require('request');

const filmNum = process.argv[2] + '/';
const filmURL = 'https://swapi-api.hbtn.io/api/films/';

// Makes an API request to get film information
request(filmURL + filmNum, async function (err, res, body) {
  if (err) return console.error(err);

  // Parse the response body to get the list of character URLs
  const charURLList = JSON.parse(body).characters;

  // Iterate through the list of character URLs
  for (const charURL of charURLList) {
    request(charURL, function (err, res, body) {
      if (err) return console.error(err);
      console.log(JSON.parse(body).name);
    });
  }
});
