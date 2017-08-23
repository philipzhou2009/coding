// https://www.toptal.com/javascript/interview-questions

'use strict';


(function (x) {
    return (function (y) {
        console.log(x);
    })(2)
})(1);

// recursively
console.log((function f(n) { return ((n > 1) ? n * f(n - 1) : n) })(10));


// Closures
// https://developer.mozilla.org/en/docs/Web/JavaScript/Closures
function makeFunc() {
    var name = 'Mozilla';
    function displayName() {
        console.log(name);
    }
    return displayName;
}

var myFunc = makeFunc();
myFunc();

// When setting an object property, 
// JavaScript will implicitly stringify the parameter value. 
// In this case, since b and c are both objects, 
// they will both be converted to "[object Object]". 
// As a result, a[b] anda[c] are both equivalent to a["[object Object]"] 
// and can be used interchangeably. 
// Therefore, setting or referencing a[c] is precisely the same as setting or referencing a[b].
var a = {},
    b = { key: 'b' },
    c = { key: 'c' };

a[b] = 123;
a[c] = 456;

console.log(a[b]);

// In JavaScript, both || and && are logical operators that return the first fully-determined “logical value” when evaluated from left to right.
console.log("0 || 1 = "+(0 || 1));
console.log("1 || 2 = "+(1 || 2));
console.log("0 && 1 = "+(0 && 1));
console.log("1 && 2 = "+(1 && 2));

// math
console.log("0 | 1 = "+(0 | 1));
console.log("1 | 2 = "+(1 | 2));
console.log("0 & 1 = "+(0 & 1));
console.log("1 & 2 = "+(1 & 2));

// 5,5,5,5,5
for (var i = 0; i < 5; i++) {
  setTimeout(function() { console.log(i); }, i * 1000 );
}
// 0, 1, 2, 3, and 4 
for (var i = 0; i < 5; i++) {
	(function(x) {
    	setTimeout(function() { console.log(x); }, x * 1000 );
    })(i);
}

// closure
var globalVar = "xyz";

function xxx(nn) {
(function outerFunc(outerArg) {
  var outerVar = 'a';
  
  (function innerFunc(innerArg) {
    var innerVar = 'b';
    
    console.log(
      "outerArg = " + outerArg + "\n" +
      "innerArg = " + innerArg + "\n" +
      "outerVar = " + outerVar + "\n" +
      "innerVar = " + innerVar + "\n" +
      "globalVar = " + globalVar + "\n" +
    "nn=" + nn);
    
  })(456);
})(123);
}

xxx(33)

console.log(1 + 0.2)
console.log(0.1 + 0.2)
console.log(0.1 + 0.2 == 0.3)

// not working in strict mode
function func() {
   return arguments.callee; 
}

const func1 = () => {
       return arguments.callee; 

}
// console.log(func(), func1())