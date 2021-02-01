package codesignal;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.*;

class CheckPalindromeTest {

    @ParameterizedTest(name = "{0} = {1}")
    @CsvSource({
            "aabaa, true",
            "abac, false",
            "a, true",
    })
    void checkPalindrome(String inputString, boolean expected) {

        boolean actual = new CheckPalindrome().checkPalindrome(inputString);
        assertEquals(expected, actual);
    }
}