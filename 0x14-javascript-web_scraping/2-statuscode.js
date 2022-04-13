#!/usr/bin/node

const { get } = require('request');
const { argv } = require('process');

get(argv[2], (err, { statusCode }) => {
  if (err) {
    return (console.log(err));
  }
  console.log('code:', statusCode);
});
