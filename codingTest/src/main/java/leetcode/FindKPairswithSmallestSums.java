package leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
 * <p>
 * Define a pair (u,v) which consists of one element from the first array and one element from the second array.
 * <p>
 * Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
 * <p>
 * Example 1:
 * <p>
 * Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
 * Output: [[1,2],[1,4],[1,6]]
 * Explanation: The first 3 pairs are returned from the sequence:
 * [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
 * Example 2:
 * <p>
 * Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
 * Output: [1,1],[1,1]
 * Explanation: The first 2 pairs are returned from the sequence:
 * [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
 * Example 3:
 * <p>
 * Input: nums1 = [1,2], nums2 = [3], k = 3
 * Output: [1,3],[2,3]
 * Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
 */
public class FindKPairswithSmallestSums {
    public List<int[]> kSmallestPairs0(int[] nums1, int[] nums2, int k) {

        List<int[]> result = new ArrayList<>();

        int length1 = nums1.length;
        int length2 = nums2.length;

        if (length1 == 0 || length2 == 0) {
            return result;
        }

        result.add(new int[]{nums1[0], nums2[0]});

        int idx1 = 0;
        int idx2 = 0;
        int c1 = 1;
        int c2 = 1;

        int counter = 1;
        while (counter < k && idx1 < length1 && idx2 < length2) {

            int i1 = nums1[idx1];
            int i2 = nums2[idx2];
            int n1 = nums1[c1];
            int n2 = nums2[c2];

            if (i1 + n2 <= i2 + n1) {
                result.add(new int[]{i1, n2});
                c2++;
                if (c2 >= length2) {
                    idx1++;
                    c2 = 0;
                }
            } else {
                result.add(new int[]{i2, n1});
                c1++;
                if (c1 >= length1) {
                    idx2++;
                    c1 = 0;
                }

            }

            counter++;
        }

        return result;
    }

    public List<int[]> kSmallestPairs(int[] nums1, int[] nums2, int k) {

        List<int[]> result = new ArrayList<>();

        int length1 = nums1.length;
        int length2 = nums2.length;

        if (length1 == 0 || length2 == 0) {
            return result;
        }


        int idx1 = 0;
        int idx2 = 0;
        int c1 = 0;
        int c2 = 0;

        int counter = 0;
        while (counter < k && idx1 < length1 && idx2 < length2) {

            if (c1 == 0 && c2 == 0) {
                result.add(new int[]{nums1[0], nums2[0]});
                c1++;
                c2++;
            } else {
                if (c2 >= length2) {
                    idx1++;
                    c2 = 0;
                    continue;
                }

                if (c1 >= length1) {
                    idx2++;
                    c1 = 0;
                    continue;
                }

                int i1 = nums1[idx1];
                int i2 = nums2[idx2];
                int n1 = nums1[c1];
                int n2 = nums2[c2];
                if (i1 + n2 <= i2 + n1) {
                    result.add(new int[]{i1, n2});
                    c2++;
                } else {
                    result.add(new int[]{i2, n1});
                    c1++;
                }

            }

            counter++;
        }

        return result;
    }

}
