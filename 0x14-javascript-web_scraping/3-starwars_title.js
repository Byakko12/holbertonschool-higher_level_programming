#!/usr/bin/node

const { get } = require('request');
const { argv } = require('process');
const url = 'https://swapi-api.hbtn.io/api/films/${argv[2]}';

get(url, (err, { statusCode }, data) => {
  if (err) {
    console.log(err);
    return;
  }
  const { titleOfStarWars } = JSON.parse(data);
  console.log(titleOfStarWars);
});
