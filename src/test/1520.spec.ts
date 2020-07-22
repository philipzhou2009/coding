const maxNumOfSubstrings = require("../main/1520");

describe.skip("1502 testing...", () => {
  test("case 1 ", () => {
    const actual = maxNumOfSubstrings("adefaddaccc");
    expect(actual).toContain("e");
    expect(actual).toContain("f");
    expect(actual).toContain("ccc");
  });

  test("case 2 ", () => {
    const actual = maxNumOfSubstrings("abbaccd");
    expect(actual).toContain("d");
    expect(actual).toContain("bb");
    expect(actual).toContain("cc");
  });

  test("case 3", () => {
    const actual = maxNumOfSubstrings("");
    expect(actual).toEqual([""]);
  });

  test("case 4", () => {
    let actual = maxNumOfSubstrings("aaaaaa");
    expect(actual).toEqual(["aaaaaa"]);
  });

  test("case 5", () => {
    let actual = maxNumOfSubstrings("abab");
    expect(actual).toEqual(["abab"]);
  });

  test("case 6", () => {
    let actual = maxNumOfSubstrings("abaabbcaaabbbccd");
    expect(actual).toEqual(["d", "abaabbcaaabbbcc"]);
  });
});
