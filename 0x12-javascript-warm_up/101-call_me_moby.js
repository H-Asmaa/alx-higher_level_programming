#!/usr/bin/node
function callMeMoby (x, theFunction) {
  if (x > 1) {
    callMeMoby(x - 1, theFunction);
  }
  theFunction();
}
module.exports = {
  callMeMoby
};
