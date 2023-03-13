#!/usr/bin/node

const lengthOfArgument = process.argv.length;

if (lengthOfArgument < 3) console.log('No argument');
if (lengthOfArgument === 3) console.log('Argument found');
if (lengthOfArgument > 3) console.log('Arguments found');
