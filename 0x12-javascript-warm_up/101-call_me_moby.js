#!/usr/bin/nod
function callMeMoby(x, theFunction) {
    if (x > 1) {
        callMeMoby(x - 1, theFunction);
    }
    if (x > 0) {
        theFunction();
    }
}
module.exports = {
    callMeMoby
};
