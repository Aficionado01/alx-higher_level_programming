#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const array = list.map((x, i) => x * i);
console.log(array);
