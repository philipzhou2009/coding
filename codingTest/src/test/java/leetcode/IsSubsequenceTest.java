package leetcode;

import org.junit.Test;

import static org.assertj.core.api.Assertions.assertThat;

public class IsSubsequenceTest {

    private IsSubsequence subject = new IsSubsequence();

    @Test
    public void isSubsequence() {

        boolean actual = subject.isSubsequence("abc", "ahbgdc");
        assertThat(actual).isTrue();

        actual = subject.isSubsequence("axc", "ahbgdc");
        assertThat(actual).isFalse();


        actual = subject.isSubsequence("abc", "ahbgd11111111111111111111111hhhhhhhhhhhhhc");
        assertThat(actual).isTrue();
    }
}