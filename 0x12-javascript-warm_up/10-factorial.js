#!/usr/bin/node
const { argv } = require('process');
function factorial (a) {
  if (!a) {
    return (1);
  }
  return (a * factorial(a - 1));
}
console.log(factorial(parseInt(argv[2])));
