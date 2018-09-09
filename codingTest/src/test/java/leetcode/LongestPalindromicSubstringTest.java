package leetcode;

import org.junit.Test;

import static org.assertj.core.api.Assertions.*;

import static org.junit.Assert.*;

public class LongestPalindromicSubstringTest {

    private LongestPalindromicSubstring subject = new LongestPalindromicSubstring();
    @Test
    public void longestPalindrome() {

        String actual = subject.longestPalindrome("babad");

        assertThat(actual).isEqualTo("bab");

        actual = subject.longestPalindrome("cbbd");
        assertThat(actual).isEqualTo("bb");

        actual = subject.longestPalindrome("1234567887654321");
        assertThat(actual).isEqualTo("1234567887654321");
    }

    @Test
    public void palindromic() {

        boolean actual;
        actual = subject.palindromic("bb");
        assertThat(actual).isTrue();

        actual = subject.palindromic("bab");
        assertThat(actual).isTrue();


        actual = subject.palindromic("bbbbbbbabbbbbbb");
        assertThat(actual).isTrue();

        actual  = subject.palindromic("baaaaaaaaaa");
        assertThat(actual).isFalse();
    }
}