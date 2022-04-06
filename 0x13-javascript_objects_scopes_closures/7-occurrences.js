#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let i = 0; list[i]; i++) {
    if (searchElement === list[i]) {
      counter += 1;
    }
  }
  return (counter);
};
