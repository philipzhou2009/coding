const maxNumOfSubstrings = require("../main/1520");

describe("1502 testing...", () => {
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
});
