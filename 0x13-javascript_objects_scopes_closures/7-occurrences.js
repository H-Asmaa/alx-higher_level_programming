#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurrences = 0;
  for (const i of list) {
    if (i === searchElement) {
      occurrences++;
    }
  }
  return occurrences;
};
