package hackerrank;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.*;

class JavaRegexTest {

    @ParameterizedTest(name = "{0} = {1}")
    @CsvSource({
            "000.12.12.034, true",
            "121.234.12.12, true",
            "23.45.12.56, true",
            "000.12.234.23.23, false",
            "666.666.23.23, false",
            ".213.123.23.32, false",
            "23.45.22.32., false",
            "I.Am.not.an.ip, false",
            "192.168.0.1, true",
            "1.1.1.1, true",
            "0.0.0.0, true"
    })
    void validateIpAddressString(String input, boolean expected) {

        boolean actual = input.matches(new JavaRegex().pattern);

        assertEquals(expected, actual);

    }
}