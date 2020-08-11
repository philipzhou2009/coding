// https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/
/**
 * @param {string} s
 * @return {string[]}
 */

let logger = true ? console.log : () => {};

var maxNumOfSubstrings = function (s) {
  logger("input:", s);

  if (s === "") {
    return [""];
  }

  let chars = s.split("");
  let charPositionsMap = new Map();
  for (let i = 0; i < chars.length; i++) {
    const targetChar = chars[i];
    const targetEntry = charPositionsMap.get(targetChar);

    if (targetEntry === undefined) {
      charPositionsMap.set(targetChar, [i, i]);
    } else {
      targetEntry[1] = i;
    }
  }
  logger(charPositionsMap);

  const mySet = new Set();

  for (const element of charPositionsMap) {
    const targetPositionLeft = element[1][0];
    const targetPostitionRight = element[1][1];
    // logger("targetPositionLeft", targetPositionLeft);
    // logger("targetPostitionRight", targetPostitionRight);

    if (targetPositionLeft > 0) {
      const sub = getValidString(
        0,
        targetPositionLeft,
        charPositionsMap,
        chars,
        s
      );
      if (sub && !mySet.has(sub)) {
        logger("firstStr:", sub);
        mySet.add(sub);
      }
    }

    const sub = getValidString(
      targetPositionLeft,
      targetPostitionRight,
      charPositionsMap,
      chars,
      s
    );
    if (sub && !mySet.has(sub)) {
      logger("firstStr:", sub);
      mySet.add(sub);
    }

    if (targetPostitionRight + 1 < s.length - 1) {
      const sub = getValidString(
        targetPostitionRight + 1,
        s.length - 1,
        charPositionsMap,
        chars,
        s
      );
      if (sub && !mySet.has(sub)) {
        logger("sub:", sub);
        mySet.add(sub);
      }
    }
  }

  mySet.add(s);

  return getResult(mySet);
};

const getValidString = (
  targetPositionLeft,
  targetPostitionRight,
  charPositionsMap,
  chars,
  s
) => {
  let foundSubString = true;
  for (
    let index = targetPositionLeft;
    index < targetPostitionRight + 1;
    index++
  ) {
    const nextChar = chars[index];
    // logger("nextChar:", nextChar);
    const nextCharPositions = charPositionsMap.get(nextChar);
    const nextCharLeft = nextCharPositions[0];
    const nextCharRight = nextCharPositions[1];
    if (
      nextCharLeft < targetPositionLeft ||
      nextCharRight > targetPostitionRight
    ) {
      foundSubString = false;
      break;
    }
  }

  if (foundSubString === true) {
    return s.substring(targetPositionLeft, targetPostitionRight + 1);
  }
  return undefined;
};

const getResult = (mySet) => {
  let maxCount = 0;
  let totalLength = 0;
  let selectedResult = undefined;

  let array = Array.from(mySet);
  logger("mySet:", array);

  //   candidate = {
  //       length: 10,
  //       count: 3,
  //       strings: []
  //   }
  const candidates = [];

  for (const element of array) {
    candidates.push({
      length: element.length,
      count: 1,
      strings: [element],
    });
  }

  for (let i = 0; i < array.length; i++) {
    const sub = array[i];
    for (const candidate of candidates) {
      const strings = candidate.strings;
      let found = false;
      for (const element of strings) {
        if (sub.includes(element) || element.includes(sub)) {
          found = true;
          break;
        }
      }
      if (found === false) {
        strings.push(sub);
        candidate.count += 1;
        candidate.length += sub.length;
      }
    }
  }

  for (const candidate of candidates) {
    if (candidate.count > maxCount) {
      maxCount = candidate.count;
      totalLength = candidate.length;
      selectedResult = candidate.strings;
    }
    if (candidate.count === maxCount) {
      if (candidate.length < totalLength) {
        totalLength = candidate.length;
        selectedResult = candidate.strings;
      }
    }
  }

  logger("candidates:", candidates);
  logger(selectedResult);

  return selectedResult;
};

module.exports = maxNumOfSubstrings;
