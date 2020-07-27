const minSubArrayLen = require("../main/209-0");

describe("209 testing...", () => {
  test("case 1", () => {
    const actual = minSubArrayLen(7, [2, 3, 1, 2, 4, 3]);
    expect(actual).toEqual(2);
  });

  test("case 2", () => {
    const actual = minSubArrayLen(4, [1, 4, 4]);
    expect(actual).toEqual(1);
  });

  test("case 3", () => {
    const actual = minSubArrayLen(11, [1, 2, 3, 4, 5]);
    expect(actual).toEqual(3);
  });

  test("case 4", () => {
    const actual = minSubArrayLen(213, [
      12,
      28,
      83,
      4,
      25,
      26,
      25,
      2,
      25,
      25,
      25,
      12,
    ]);
    expect(actual).toEqual(8);
  });

  test("case 5", () => {
    const actual = minSubArrayLen(6, [10, 2, 3]);
    expect(actual).toEqual(1);
  });
});
