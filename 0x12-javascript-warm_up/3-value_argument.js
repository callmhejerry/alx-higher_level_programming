#!/usr/bin/node

const argv = process.argv;
const firstArgument = argv[2];

if (firstArgument) console.log(firstArgument);
else console.log('No argument');
