// https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/
/**
 * @param {string} s
 * @return {string[]}
 */
var maxNumOfSubstrings = function (s) {
  console.log("input:", s);

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

  console.log(charPositionsMap);

  //   {
  //       totalLength: 10,
  //       count: 3,
  //       strings: []
  //   }
  const candidates = [];
  const mySet = new Set();

  charPositionsMap.forEach((value, key) => {
    console.log("for char:", key);
    const targetPositionLeft = value[0];
    const targetPostitionRight = value[1];

    let foundSubString = true;
    let farRight = value[1];
    let farLeft = value[0];
    for (
      let index = targetPositionLeft + 1;
      index < targetPostitionRight;
      index++
    ) {
      const nextChar = chars[index];
      //   console.log("nextChar:", nextChar);
      const nextCharPositions = charPositionsMap.get(nextChar);
      const nextCharLeft = nextCharPositions[0];
      const nextCharRight = nextCharPositions[1];
      if (
        nextCharLeft < targetPositionLeft ||
        nextCharRight > targetPostitionRight
      ) {
        foundSubString = false;
        // break;
        if (nextCharRight > farRight) {
          farRight = nextCharRight;
        }
        if (nextCharLeft < farLeft) {
          console.log();
          farLeft = nextCharLeft;
        }
      }
    }

    console.log("farLeft=", farLeft);
    console.log("farRight", farRight);

    const newSub = s.substring(farLeft, farRight + 1);
    if (!mySet.has(newSub)) {
      mySet.add(newSub);
      console.log("found newSub 1:", newSub);
      updateCandidates(candidates, newSub);
      console.log("candidates 1:", candidates);
    }

    // combine with left chars
    for (let i = farRight + 1; i < s.length; i++) {
      const nextChar = chars[i];
      const nextCharPositions = charPositionsMap.get(nextChar);
      const nextCharLeft = nextCharPositions[0];
      const nextCharRight = nextCharPositions[1];

      if (nextCharLeft < farLeft || nextCharRight > i) {
        foundSubString = false;
        continue;
      }

      const newSub = s.substring(farLeft, nextCharRight + 1);
      if (!mySet.has(newSub)) {
        console.log("found newSub 2:", newSub);
        mySet.add(newSub);
        updateCandidates(candidates, newSub);
        console.log("candidates 2:", candidates);
      }
    }
  });

  console.log("candidates:", candidates);

  let totalLength = 0;
  let maxCount = 0;
  let selectedOnes = undefined;
  for (const candidate of candidates) {
    if (maxCount === 0 || candidate.count > maxCount) {
      totalLength = candidate.totalLength;
      maxCount = candidate.count;
      selectedOnes = candidate.strings;
      continue;
    }
    if (candidate.count === maxCount) {
      if (candidate.totalLength < totalLength) {
        totalLength = candidate.totalLength;
        maxCount = candidate.count;
        selectedOnes = candidate.strings;
      }
    }
  }

  console.log("selectedOnes:", selectedOnes);
  //   if (selectedOnes === undefined) {
  //     return [s];
  //   }

  return selectedOnes;
};

const updateCandidates = (candidates, newSub) => {
  //   console.log("candidates:", candidates);
  //   console.log("newSub:", newSub);

  let inserted = false;
  for (let candidate of candidates) {
    let found = true;
    const subStrings = candidate.strings;
    console.log("subStrings:", subStrings);
    for (let sub of subStrings) {
      console.log("here sub=", sub);
      if (sub.includes(newSub) === true || newSub.includes(sub) === true) {
        found = false;
        break;
      }
    }

    // console.log("found:", found);

    if (found === true) {
      inserted = true;
      // time to insert
      candidate.count += 1;
      candidate.totalLength += newSub.length;
      candidate.strings.push(newSub);
    }
  }

  if (inserted === false) {
    candidates.push({
      count: 1,
      totalLength: newSub.length,
      strings: [newSub],
    });
  }
};

module.exports = maxNumOfSubstrings;
