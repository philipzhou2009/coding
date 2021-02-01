package com.leetcode.problem0925;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Solution01Test {

    @ParameterizedTest(name = "{0}, {1} = {2}")
    @CsvSource({
            "alex, aaleex, true",
            "saeed, ssaaedd, false",
            "leelee, lleeelee, true",
            "laiden, laiden, true",
            "alex, aaleexa, false",
            "alexd, ale, false"
    })
    void isLongPressedName(String first, String second, boolean expectedResult) {
        Solution01 subject = new Solution01();
        boolean actual = subject.isLongPressedName(first, second);
        assertEquals(actual, expectedResult);
    }
}