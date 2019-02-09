function addOne(x) {     // Conventional way.
    return x + 1;
}
var six = addOne(5);

var addOne = function(x) {    // 1st alternate way.  // although it reminds us a bit of how object methods are defined[addOne : function() {}]
    return x + 1;
} ;
var six = addOne(5);  