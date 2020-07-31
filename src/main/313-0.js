// https://leetcode.com/problems/super-ugly-number/
/**
 * @param {number} n
 * @param {number[]} primes
 * @return {number}
 */

let logger = true ? console.log : () => {};

var nthSuperUglyNumber = function (n, primes) {
  const primesLength = primes.length;

  const firstE = primes[0];
  let newSet = new Set();
  let newArray = [];
  let cursor1 = 0;

  const array = primes;
  let sum = getSum(n, primes);
  logger("sum=", sum);

  for (let i = 0; i < primes.length; i++) {
    const element = primes[i];

    let newElement = firstE * element;
    // logger(newElement);

    while (primes[cursor1] < newElement) {
      // newArray.push(primes[cursor1]);
      newSet.add(primes[cursor1]);
      cursor1++;
    }

    // newArray.push(newElement);
    newSet.add(newElement);
  }

  newArray = Array.from(newSet);
  logger(newArray);

  let anotherSum = getSum(n, newArray);
  logger("antherSum=", anotherSum);

  if(sum !== anotherSum) {
    nthSuperUglyNumber(n, newArray);
    
  } else {
    logger("result=", newArray);

  }

};

const getSum = (n, array) => {
  let sum = 0;
  for (let i = 0; i < n; i++) {
    if (i >= array.length) {
      break;
    }
    const element = array[i];
    sum += element;
  }

  return sum;
};

module.exports = nthSuperUglyNumber;
