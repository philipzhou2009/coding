package fbsamples;

import org.junit.Test;

import static org.assertj.core.api.Assertions.assertThat;

public class EditDistanceTest {


    private String word1;
    private String word2;
    private boolean actual;

    @Test
    public void solution() {

        word1 = "abc";
        word2 = "bbc";

        actual = EditDistance.solution(word1, word2);
        assertThat(actual).isEqualTo(true);

        word1 = "abc";
        word2 = "aaa";

        actual = EditDistance.solution(word1, word2);
        assertThat(actual).isEqualTo(false);


        word1 = "abcd";
        word2 = "abc";
        actual = EditDistance.solution(word1, word2);
        assertThat(actual).isEqualTo(true);

        word1 = "abc";
        word2 = "abbc";
        actual = EditDistance.solution(word1, word2);
        assertThat(actual).isEqualTo(true);

    }
}