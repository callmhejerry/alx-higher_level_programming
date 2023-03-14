#!/usr/bin/node

function nbOccurences (list, searchElement) {
  let numOfOccuerences = 0;

  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      numOfOccuerences++;
    }
  }
  return numOfOccuerences;
}

exports.nbOccurences = nbOccurences;
