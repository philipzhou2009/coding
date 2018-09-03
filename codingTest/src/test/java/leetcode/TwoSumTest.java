package leetcode;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.Test;

import static org.junit.Assert.*;

public class TwoSumTest {

    @Test
    public void twoSum() {

        int[] actual = TwoSum.twoSum(new int[]{2, 7, 11, 15}, 26);

        assertThat(actual[0]).isEqualTo(2);
        assertThat(actual[1]).isEqualTo(3);
    }
}