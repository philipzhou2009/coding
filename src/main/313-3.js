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
  let flag = array[0] === 2 ? true : false;

  while (true) {
    if (flag === false && element % 2 === 0) {
      element++;
    }

    if (isUgly(element, array, aLength) === true) {
      logger("found", element);
      counter++;
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

const isUgly = (target, array, nLength) => {
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
    }
  }

  return false;
};

// nthSuperUglyNumber(12, [2, 7, 13, 19]);

module.exports = nthSuperUglyNumber;
