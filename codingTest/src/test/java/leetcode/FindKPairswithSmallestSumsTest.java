package leetcode;

import org.junit.Test;

import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;

public class FindKPairswithSmallestSumsTest {

    private FindKPairswithSmallestSums subject = new FindKPairswithSmallestSums();

    @Test
    public void kSmallestPairs() {

        List<int[]> actual = subject.kSmallestPairs(new int[]{1, 7, 11}, new int[]{2, 4, 6}, 3);

        assertThat(actual).containsExactly(
                new int[]{1, 2},
                new int[]{1, 4},
                new int[]{1, 6}
        );

        actual = subject.kSmallestPairs(new int[]{1, 1, 2}, new int[]{1, 2, 3}, 2);

        assertThat(actual).containsExactly(
                new int[]{1, 1},
                new int[]{1, 1}
        );

        actual = subject.kSmallestPairs(new int[]{1, 2}, new int[]{3}, 3);

        assertThat(actual).containsExactly(
                new int[]{1, 3},
                new int[]{2, 3}
        );
    }
}