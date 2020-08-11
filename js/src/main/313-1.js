// https://leetcode.com/problems/super-ugly-number/
/**
 * @param {number} n
 * @param {number[]} primes
 * @return {number}
 */

let logger = false ? console.log : () => {};

var nthSuperUglyNumber = function (n, primes) {
  logger("======================");

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
  return recursive(n, array, index);
};

const recursive = (n, array, lastIndex) => {
  logger("array=", array);

  let anotherArray = [];
  for (let i = 0; i < array.length; i++) {
    const ie = array[i] * array[lastIndex];
    anotherArray.push(ie);
  }
  logger("anotherArray", anotherArray);

  // merge 2 arraies
  let cursor1 = 0;
  let cursor2 = 0;
  let newArray = [];
  let lastPushed = 0;
  let counter = 0;
  while (true) {
    if (cursor1 >= array.length) {
      for (let j = cursor2; j < anotherArray.length; j++) {
        const je = anotherArray[j];
        if (je === lastPushed) {
          continue;
        }
        newArray.push(je);
        counter++;
        if (counter > n + 1) {
          break;
        }
        lastPushed = je;
      }
      break;
    }

    if (cursor2 >= anotherArray.length) {
      for (let j = cursor1; j < array.length; j++) {
        const je = array[j];
        if (je === lastPushed) {
          continue;
        }
        newArray.push(je);
        lastPushed = je;

        counter++;
        if (counter > n + 1) {
          break;
        }
      }
      break;
    }

    if (array[cursor1] < anotherArray[cursor2]) {
      newArray.push(array[cursor1]);
      lastPushed = array[cursor1];
      cursor1++;

      counter++;
      if (counter > n + 1) {
        break;
      }
    } else if (array[cursor1] > anotherArray[cursor2]) {
      newArray.push(anotherArray[cursor2]);
      lastPushed = anotherArray[cursor2];
      cursor2++;

      counter++;
      if (counter > n + 1) {
        break;
      }
    } else {
      newArray.push(array[cursor1]);
      lastPushed = array[cursor1];
      cursor1++;
      cursor2++;

      counter++;
      if (counter > n + 1) {
        break;
      }
    }
  }

  logger("newArray", newArray);
  // newArray = newArray.slice(0, n+1);

  if (lastIndex < n) {
    lastIndex++;
    return recursive(n, newArray, lastIndex);
  } else {
    logger("resultArray", newArray);
    let result = newArray[n - 1];
    logger("result", result);
    return result;
  }
};

module.exports = nthSuperUglyNumber;
