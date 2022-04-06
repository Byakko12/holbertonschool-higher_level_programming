#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = [];
  for (let i = 0; list[i]; i++) {
    reversedList.unshift(list[i]);
  }
  return (reversedList);
};
