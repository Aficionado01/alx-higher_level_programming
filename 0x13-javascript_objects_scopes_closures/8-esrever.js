#!/usr/bin/node
exports.esrever = function (list) {
  const reverse = [];
  for (const i of list) {
    reverse.unshift(i);
  }
  return reverse;
};
