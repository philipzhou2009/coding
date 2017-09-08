// appendChildren()
// registerHandlers()
// registerClickHandler()
// console.log(formatDate("12/31/2014"));
// console.log(removeProperty({ name: "aaa", addr: undefined }, "addr"))

// Ensure: https://www.testdome.com/for-developers/solve-question/8649
function ensure(value) {

    if (arguments.length === 0 || value === undefined) {
        throw "arguments error"
    }

    return value
}

// Remove Property
function removeProperty(obj, prop) {

    if (prop in obj) {
        delete obj[prop];
        return true
    }

    return false;
}

// Date
function formatDate(userDate) {
    var arr = userDate.split('/');

    var day = (arr[1].length <= 1) ? '0' + arr[1] : arr[1];
    var mon = (arr[0].length <= 1) ? '0' + arr[0] : arr[0];

    var result = arr[2] + mon + day;

    return result;
}

// Image Gallery
function registerClickHandler() {
    // Implement the click handler here for button of class 'remove'
    var x = document.getElementsByClassName("remove");
    var i;
    for (i = 0; i < x.length; i++) {
        // x[i].style.backgroundColor = "red";
        x[i].onclick = function (e) {
            console.log("onclick")
            this.parentNode.parentNode.removeChild(this.parentNode)

        };
    }
}

// Closures
function registerHandlers() {
    var as = document.getElementsByTagName('a');
    for (var i = 0; i < as.length; i++) {
        as[i].onclick = alertI(i)
    }
}

function alertI(i) {
    return function () {
        alert(i);
        return false;

    }
}

// Loop
function appendChildren() {
    var allDivs = document.getElementsByTagName("div");
  
    var length = allDivs.length
    for (var i = 0; i < length; i++) {
      var newDiv = document.createElement("div");
      decorateDiv(newDiv);
      var node = allDivs[i]
      node.appendChild(newDiv);
    }
  }
  
  // Mock of decorateDiv function for testing purposes
  function decorateDiv(div) { }