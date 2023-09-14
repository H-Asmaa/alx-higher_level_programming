#!/usr/bin/node
exports.converter = function (base) {
  return function decimalConverter (decimal) {
    return decimal.toString(base);
  };
};
/* A code that i was working on before i know the toString can do all of this.
exports.converter = function (base) {
    return function decimalConverter(decimal) {
        if (decimal > 0) {
            decimalConverter(Math.floor(decimal / base));
            if ((decimal % base) < 10) {
                return (decimal % base).toString();
            } else {
                return String.fromCharCode(65 + (decimal % base) - 10);
            }
        }
    }
} */
