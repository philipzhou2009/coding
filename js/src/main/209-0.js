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
  let resultLength = 0;
  const numsLength = nums.length;
  let sum = 0;
  let currentLength = 0;
  let lastSum = 0;
  let travelUntil = numsLength;

  for (let i = 0; i < numsLength; i++) {
    sum = 0;
    currentLength = 0;

    if (resultLength > 0) {
      logger("lastSum", lastSum);
      logger("nums[i-1]", nums[i - 1]);
      if (lastSum - nums[i - 1] >= s) {
        lastSum -= nums[i - 1];
        resultLength -= 1;
        logger("resultLength here", resultLength);
        logger("i=", i, "value=", nums[i]);
        continue;
      }
    }

    lastSum = 0;
    travelUntil = numsLength;
    if (resultLength !== 0 && i + resultLength - 1 < numsLength) {
      travelUntil = i + resultLength - 1;
    }

    logger("left:", i, "right:", travelUntil);

    for (let j = i; j < travelUntil; j++) {
      sum += nums[j];
      // tmpArray.push(je);
      currentLength++;
      lastSum = sum;
      if (sum >= s) {
        // logger("found!");
        if (resultLength === 0 || currentLength < resultLength) {
          resultLength = currentLength;
          logger("resultLength haha", resultLength);
          // resultArray = tmpArray;
        }
        // logger("found!", lastSum, tmpArray);
        break;
      }
    }
  }

  // logger(resultArray);
  return resultLength;
};

module.exports = minSubArrayLen;
