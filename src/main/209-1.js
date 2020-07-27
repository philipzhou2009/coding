/**
 * @param {number} s
 * @param {number[]} nums
 * @return {number}
 */
/*
Example: 
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
*/

let logger = true ? console.log : () => {};

var minSubArrayLen = function (s, nums) {
  let resultArray = [];
  let resultLength = 0;
  let resultSum = 0;
  let tmpArray = [];

  const numsLength = nums.length;
  let sum = nums[0];

  for (let i = 0; i < numsLength; i++) {
    tmpArray = [];
    sum = 0;

    for (let j = i; j < numsLength; j++) {
      const je = nums[j];
      sum += je;
      tmpArray.push(je);
      if (sum >= s) {
        logger("found", tmpArray);
        if (resultLength === 0 || resultLength > tmpArray.length) {
          resultLength = tmpArray.length;
          resultArray = tmpArray;
        }
        break;
      }
    }
  }

  logger(resultArray);
  return resultLength;
};

module.exports = minSubArrayLen;
