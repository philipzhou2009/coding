// https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/
/**
 * @param {string} s
 * @return {string[]}
 */

let logger = false ? console.log : () => {};

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

  //   {
  //       totalLength: 10,
  //       count: 3,
  //       strings: []
  //   }
  const candidates = [];
  const mySet = new Set();

  charPositionsMap.forEach((value, key) => {
    logger("for char:", key);
    const targetPositionLeft = value[0];
    const targetPostitionRight = value[1];

    let foundSubString = true;
    let farRight = value[1];
    let farLeft = value[0];

    let newSub = getValidString(
      targetPositionLeft,
      targetPostitionRight,
      charPositionsMap,
      chars,
      s
    );
    if (newSub !== undefined && !mySet.has(newSub)) {
      mySet.add(newSub);
      logger("found newSub 1:", newSub);
    }

    // combine with left chars
    for (let i = farRight + 1; i < s.length; i++) {
      newSub = getValidString(
        targetPositionLeft,
        i,
        charPositionsMap,
        chars,
        s
      );
      if (newSub !== undefined && !mySet.has(newSub)) {
        mySet.add(newSub);
        logger("found newSub 2:", newSub);
      }
    }
  });

  selectedOnes = getResult(mySet);
  logger("selectedOnes:", selectedOnes);
  return selectedOnes;
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
    //   logger("nextChar:", nextChar);
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
