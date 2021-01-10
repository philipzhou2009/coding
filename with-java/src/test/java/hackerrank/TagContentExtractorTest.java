package hackerrank;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.*;

class TagContentExtractorTest {

    @ParameterizedTest(name = "{0} => {1}")
    @CsvSource({
            "<h1>Nayeem loves counseling</h1>, Nayeem loves counseling",
            "<h1><h1>Sanjay has no watch</h1></h1><par>So wait for a while</par>, xxx",
            "<Amee>safat codes like a ninja</amee>, None",
            "<SA premium>Imtiaz has a secret crush</SA premium>, Imtiaz has a secret crush"

    })
    void extractor(String input, String expected) {

        String actual = new TagContentExtractor().extractor(input);
        assertEquals(expected, actual);
        System.out.println("======================");

    }
}