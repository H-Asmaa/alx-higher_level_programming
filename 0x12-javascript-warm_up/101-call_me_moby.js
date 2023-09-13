#!/usr/bin/no
function callMeMoby (x, theFunction) {
  if (x > 0) {
    callMeMoby(x - 1, theFunction);
    theFunction();
  }
}
module.exports = {
  callMeMoby
};
