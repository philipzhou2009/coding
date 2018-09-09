package leetcode;

/**
 * Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
 * <p>
 * Example 1:
 * <p>
 * Input: "babad"
 * Output: "bab"
 * Note: "aba" is also a valid answer.
 * Example 2:
 * <p>
 * Input: "cbbd"
 * Output: "bb"
 */
class LongestPalindromicSubstring {

    String longestPalindrome(String s) {

        String result = "";

        int length = s.length();
        if (s.isEmpty() || length < 2) {
            return s;
        }


        int c1 = 0;
        int c2 = 1;

        while (c1 < (length - result.length())) {

            while (c2 < length) {
                String sub = s.substring(c1, c2 + 1);
                if (palindromic(sub) && sub.length() > result.length()) {
                    result = sub;
                }
                c2++;
            }

            c1++;
            c2 = c1 + result.length();
        }

        return result;

    }

    boolean palindromic(String s) {

        int c = 0;
        int length = s.length();
        while (c < length / 2) {

            if (s.charAt(c) != s.charAt(length - c - 1)) {
                return false;
            }

            c++;
        }

        return true;
    }
}
