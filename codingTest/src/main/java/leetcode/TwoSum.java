package leetcode;


/**
 * Given an array of integers, return indices of the two numbers such that they add up to a specific target.
 * <p>
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * <p>
 * Example:
 * <p>
 * Given nums = [2, 7, 11, 15], target = 9,
 * <p>
 * Because nums[0] + nums[1] = 2 + 7 = 9,
 * return [0, 1].
 */
class TwoSum {

    static int[] twoSum(int[] nums, int target) {

        int[] result = new int[2];

        for (int i = 0; i < nums.length; i++) {
            int first = nums[i];

            for (int j = 0; j < nums.length; j++) {

                if (j == i) {
                    continue;
                }

                int second = nums[j];

                if (first + second == target) {
                    result[0] = i;
                    result[1] = j;

                    return result;
                }
            }
        }

        return result;

    }
}
