#!/usr/bin/node
exports.converter = function (base) {
  return function pass (number) {
    return (number).toString(base);
  };
};
