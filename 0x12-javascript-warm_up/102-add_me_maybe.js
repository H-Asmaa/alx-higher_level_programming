#!/usr/bin/node
module.exports = {
  addMeMaybe: function (nb, func) {
    nb++;
    func(nb);
  }
};
