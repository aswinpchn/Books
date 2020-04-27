//var a; a[0] = 1 ; a.push(1); // This will throw out an error saying property 0 is undefined, meaning JS doesn't consider as an array. (and also push not a property.)
var a = []; a[0] = 1; a[1] = 9; //you have to be careful about which index you’re adding by this method, It could create sparse array.
a.push(5);
var b = new Array (); // var b = [];   // The both are same.
console.log(a);
console.log(b);


var k = {};     // Same as array for objects, var k; // This will say rate is not a property when we try to assign.
k.rate = 1;
console.log(k);