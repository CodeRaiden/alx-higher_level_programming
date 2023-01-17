#!/usr/bin/node
// Script gets the contents of a webpage and stores it in a file
const request = require('request');
request(process.argv[2], (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    const fs = require('fs');
    fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
