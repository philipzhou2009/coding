const nthSuperUglyNumber = require("../main/313-3");

describe("313 tests", () => {
  test("case 0", () => {
    const actual = nthSuperUglyNumber(8, [5, 7]);
    expect(actual).toEqual(175);
  });

  test("case 1", () => {
    const actual = nthSuperUglyNumber(12, [2, 7, 13, 19]);
    expect(actual).toEqual(32);
  });

  test.only("case 2", () => {
    const actual = nthSuperUglyNumber(100000, [
      7,
      19,
      29,
      37,
      41,
      47,
      53,
      59,
      61,
      79,
      83,
      89,
      101,
      103,
      109,
      127,
      131,
      137,
      139,
      157,
      167,
      179,
      181,
      199,
      211,
      229,
      233,
      239,
      241,
      251,
    ]);
    expect(actual).toEqual(7796273);
  });
});
