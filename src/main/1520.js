// https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/
/**
 * @param {string} s
 * @return {string[]}
 */
var maxNumOfSubstrings = function (s) {
  if (s === "") {
    return [""];
  }

  let chars = s.split("");
  //   console.log(chars);

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

  //   Map {
  //     'a' => [ 0, 7 ],
  //     'd' => [ 1, 6 ],
  //     'e' => [ 2, 2 ],
  //     'f' => [ 3, 3 ],
  //     'c' => [ 8, 10 ] }
  console.log(charPositionsMap);

  const candidates = [];
  let minLength = 0;
  let maxCount = 0;
  let selectedOnes = undefined;

  charPositionsMap.forEach((value, key) => {
    // console.log("for key=", key);
    const targetMin = value[0];
    const targetMax = value[1];

    let ok = true;
    for (let j = targetMin + 1; j < targetMax; j++) {
      const nextChar = chars[j]; // d
      const nextPositions = charPositionsMap.get(nextChar); // [ 1, 6 ]
      if (targetMin > nextPositions[0] || targetMax < nextPositions[1]) {
        ok = false;
        break;
      }
    }

    if (ok === true) {
      const subString = s.substring(targetMin, targetMax + 1);
      console.log("found substring=", subString);
      let inserted = false;

      for (let candidate of candidates) {
        const positions = candidate.positions;
        if (value[0] > positions[positions.length - 1][1]) {
          inserted = true;
          candidate.positions.push(value);
          candidate.length += subString.length;
          candidate.count += 1;
          candidate.subStrings.push(subString);

          if (candidate.count > maxCount) {
            maxCount = candidate.count;
          }
        }
      }
      if (inserted === false) {
        const candidate = {
          positions: [value],
          length: subString.length,
          count: 1,
          subStrings: [subString],
        };

        candidates.push(candidate);

        if (candidate.count > maxCount) {
          maxCount = candidate.count;
        }
      }
    }

    console.log("maxCount", maxCount);
  });

  console.log("candidates", JSON.stringify(candidates));

  for (let element of candidates) {
    if (element.count === maxCount) {
      if (minLength === 0) {
        minLength = element.length;
        selectedOnes = element.subStrings;
      } else {
        minLength = element.length < minLength ? element.length : minLength;
        selectedOnes = element.subStrings;
      }
    }
  }

  console.log("selectedOnes", selectedOnes);

  if (selectedOnes === undefined) {
    return [s];
  }

  return selectedOnes;
};

module.exports = maxNumOfSubstrings;
