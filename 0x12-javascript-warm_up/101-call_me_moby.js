#!/usr/bin/nod
function callMeMoby (x, theFunction) {
  if (x >= 1) {
    if (x > 1) {
      callMeMoby(x - 1, theFunction);
    }
    theFunction();
  }
}
module.exports = {
  callMeMoby
};
