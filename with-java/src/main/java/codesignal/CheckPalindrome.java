package codesignal;

public class CheckPalindrome {

    boolean checkPalindrome(String inputString) {

        int len = inputString.length();
        char[] charArr = inputString.toCharArray();

        int cursorLeft = 0;
        int cursorRight = len - 1;

        boolean result = true;
        while (cursorLeft <= cursorRight) {

            if (charArr[cursorLeft] != charArr[cursorRight]) {
                result = false;
                break;
            }

            cursorLeft++;
            cursorRight--;
        }


        return result;
    }
}
