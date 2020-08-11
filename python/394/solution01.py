# https://leetcode.com/problems/decode-string/

logger = print if False else lambda *arg: None


class Solution:
    def decodeString(self, s: str) -> str:
        return decode(s)


def decode(s: str) -> str:
    logger("input", s)

    rightBracketIdx = s.find("]")
    if rightBracketIdx == -1:
        return s

    leftBracketIdx = s[:rightBracketIdx].rfind("[")

    i = leftBracketIdx - 1
    while True:
        if s[i].isnumeric():
            i -= 1
        else:
            i += 1
            break

    strInBrackets = s[leftBracketIdx + 1 : rightBracketIdx]
    numberStr = s[i:leftBracketIdx]

    logger("number", numberStr)
    logger("string", strInBrackets)

    j = 0
    str2 = ""
    while j < int(numberStr):
        str2 += strInBrackets
        j += 1

    logger("str2", str2)

    resultStr = s[0:i] + str2 + s[rightBracketIdx + 1 :]
    logger("resultStr", resultStr)

    return decode(resultStr)
