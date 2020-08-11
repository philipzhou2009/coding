// https://leetcode.com/problems/super-ugly-number/
/**
 * @param {number} n
 * @param {number[]} primes
 * @return {number}
 */
const { MinPriorityQueue } = require("@datastructures-js/priority-queue");

let logger = false ? console.log : () => {};

var nthSuperUglyNumber = function (n, primes) {
  let array = primes;
  let mpQueue = new MinPriorityQueue();
  mpQueue.enqueue(1, 1);
  let cursor = 0;
  let result;
  while (cursor < n) {
    let i = mpQueue.dequeue();
    let ie = i.element;
    logger("dequeue", ie);
    result = ie;
    while (mpQueue.size() > 0 && mpQueue.front().element === ie) {
      mpQueue.dequeue();
      continue;
    }

    for (const iterator of array) {
      let ne = ie * iterator;
      mpQueue.enqueue(ne, ne);
    }

    cursor++;
  }

  logger("result", result);
  return result;
};

// nthSuperUglyNumber(12, [2, 7, 13, 19]);
module.exports = nthSuperUglyNumber;
