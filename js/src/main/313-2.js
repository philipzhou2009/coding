// https://leetcode.com/problems/super-ugly-number/
/**
 * @param {number} n
 * @param {number[]} primes
 * @return {number}
 */

let logger = false ? console.log : () => {};

var nthSuperUglyNumber = function (n, primes) {
  let array = [];
  if (primes[0] !== 1) {
    array[0] = 1;
    for (const e of primes) {
      array.push(e);
    }
  } else {
    array = primes;
  }

  let index = 0;
  let newArray = array;
  let lastMaxium = 0;
  while (index < n + 1) {
    newArray = getNewArray(n, newArray, index);
    if (lastMaxium === 0 && newArray.length >= n) {
      lastMaxium = newArray[n - 1];
    } else if (
      lastMaxium !== 0 &&
      newArray.length >= n &&
      newArray[n - 1] > lastMaxium
    ) {
      break;
    }

    index++;
  }

  logger("resultArray", newArray);

  let result = newArray[n - 1];
  logger("result", result);
  return result;
};

const getNewArray = (n, array, lastIndex) => {
  logger("======================");
  logger("array[lastIndex]", array[lastIndex]);
  logger("input array=", array);

  let arrayLength = array.length;
  let cursor = 0;
  let anotherArray = [];
  let lastPushed = 0;
  for (let i = 0; i < arrayLength; i++) {
    const ie = array[i] * array[lastIndex];

    while (cursor < arrayLength) {
      if (array[cursor] <= ie && array[cursor] !== lastPushed) {
        anotherArray.push(array[cursor]);
        lastPushed = array[cursor];
        cursor++;
      } else {
        break;
      }
    }

    if (ie !== lastPushed) {
      anotherArray.push(ie);
      lastPushed = ie;
    }

    if (anotherArray.length > n) {
      break;
    }
  }

  logger("output array", anotherArray);
  return anotherArray;
};

// nthSuperUglyNumber(12, [2, 7, 13, 19]);

module.exports = nthSuperUglyNumber;
