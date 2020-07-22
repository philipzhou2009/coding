const maxNumOfSubstrings1 = require("../main/1520-1");

describe("1502-1 testing...", () => {
  test("case 1 ", () => {
    const actual = maxNumOfSubstrings1("adefaddaccc");
    expect(actual).toContain("e");
    expect(actual).toContain("f");
    expect(actual).toContain("ccc");
  });

  test("case 2 ", () => {
    const actual = maxNumOfSubstrings1("abbaccd");
    expect(actual).toContain("d");
    expect(actual).toContain("bb");
    expect(actual).toContain("cc");
  });

  test("case 3", () => {
    const actual = maxNumOfSubstrings1("");
    expect(actual).toEqual([""]);
  });

  test("case 4", () => {
    let actual = maxNumOfSubstrings1("aaaaaa");
    expect(actual).toEqual(["aaaaaa"]);
  });

  test("case 5", () => {
    let actual = maxNumOfSubstrings1("abab");
    expect(actual).toEqual(["abab"]);
  });

  test("case 6", () => {
    let actual = maxNumOfSubstrings1("abaabbcaaabbbccd");
    expect(actual).toContain("d");
    expect(actual).toContain("abaabbcaaabbbcc");
  });

  test.only("case 7", () => {
    let actual = maxNumOfSubstrings1("cabcccbaa");
    expect(actual).toEqual(["cabcccbaa"]);
  });
});
