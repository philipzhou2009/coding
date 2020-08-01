// https://leetcode.com/problems/super-ugly-number/
/**
 * @param {number} n
 * @param {number[]} primes
 * @return {number}
 */

let logger = false ? console.log : () => {};

var nthSuperUglyNumber = function (n, primes) {
  let array = primes;
  let element = array[0];
  let counter = 1;
  let aLength = array.length;
  let newArray = [1];

  while (true) {
    if (isUgly(element, array, aLength, newArray) === true) {
      logger("found", element);
      counter++;
    //   newArray.push(element);
    }

    if (counter >= n) {
      break;
    }

    element++;
  }

  let result = element;
  logger("result", element);
  return result;
};

const isUgly = (target, array, nLength, newArray) => {
  let tmp = target;
  let i = 0;

  //   logger(target, array);
  while (true) {
    if (i >= nLength) {
      break;
    }

    let element = array[i++];
    while (tmp % element === 0) {
      tmp = tmp / element;
      if (tmp === 1) {
        return true;
      }
    //   if (newArray.includes(tmp)) {
    //     return true;
    //   }
    }
  }

  return false;
  //   return tmp === 1 ? true : false;
};

// nthSuperUglyNumber(12, [2, 7, 13, 19]);

module.exports = nthSuperUglyNumber;
