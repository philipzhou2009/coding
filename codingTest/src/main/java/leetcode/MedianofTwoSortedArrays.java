package leetcode;

/**
 * There are two sorted arrays nums1 and nums2 of size m and n respectively.
 * <p>
 * Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
 * <p>
 * You may assume nums1 and nums2 cannot be both empty.
 * <p>
 * Example 1:
 * <p>
 * nums1 = [1, 3]
 * nums2 = [2]
 * <p>
 * The median is 2.0
 * Example 2:
 * <p>
 * nums1 = [1, 2]
 * nums2 = [3, 4]
 * <p>
 * The median is (2 + 3)/2 = 2.5
 */
class MedianofTwoSortedArrays {

    double findMedianSortedArrays(int[] nums1, int[] nums2) {

        double result;

        int length1 = nums1.length;
        int length2 = nums2.length;
        int total = length1 + length2;
        int pos = (length1 + length2) / 2 + 1;
        int[] resultArr = new int[pos];

        int cursor1 = 0;
        int cursor2 = 0;
        int cursor = 0;

        while (true) {
            if (cursor == pos) {
                if (total % 2 == 0) {
                    // even
                    result = ((double) (resultArr[cursor - 1] + nums2[cursor - 2])) / 2;
                } else {
                    result = (double) resultArr[cursor - 1];
                }
                break;
            }

            if (nums1[cursor1] < nums2[cursor2] && cursor1 + 1 < length1) {
                resultArr[cursor++] = nums1[cursor1++];
            } else {
                resultArr[cursor++] = nums2[cursor2++];
            }

        }

        return result;
    }

}
