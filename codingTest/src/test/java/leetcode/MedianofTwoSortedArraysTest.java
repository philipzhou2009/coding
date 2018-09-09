package leetcode;

import org.junit.Test;

import static org.assertj.core.api.Assertions.assertThat;

public class MedianofTwoSortedArraysTest {

    private MedianofTwoSortedArrays subject = new MedianofTwoSortedArrays();

    @Test
    public void findMedianSortedArrays_case1() {

        int[] num1 = {1, 3};
        int[] num2 = {2};

        double actual = subject.findMedianSortedArrays(num1, num2);

        assertThat(actual).isEqualTo(2.0);

    }

    @Test
    public void findMedianSortedArrays_case2() {

        int[] num1 = {1, 2};
        int[] num2 = {3, 4};

        double actual = subject.findMedianSortedArrays(num1, num2);

        assertThat(actual).isEqualTo(2.5);

    }

    @Test
    public void findMedianSortedArrays_case3() {

        int[] num1 = {1, 2};
        int[] num2 = {13, 14, 15, 16};

        double actual = subject.findMedianSortedArrays(num1, num2);

        assertThat(actual).isEqualTo(13.5);

    }
}