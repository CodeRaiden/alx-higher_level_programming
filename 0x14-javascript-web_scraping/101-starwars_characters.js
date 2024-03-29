#!/usr/bin/node
// Print all characters of a Star Wars movie
let request = require('request');
let movie = 'https://swapi-api.alx-tools.com/api/films/';

request.get(movie + process.argv[2], function (err, response, body) {
  if (err) throw err;
  if (response.statusCode === 200) {
    let everything = JSON.parse(body);
    let listch = [];
    for (let charac of everything.characters) {
      listch.push(new Promise(function (resolve, reject) {
        request.get(charac, function (err, response, body) {
          if (err) throw err; if (response.statusCode === 200) { resolve(JSON.parse(body).name); } else { reject(Error('Unknown')); }
        });
      }));
    }
    Promise.all(listch).then(function (names) {
      names.forEach(function (name) {
        console.log(name);
      });
    });
  }
});
