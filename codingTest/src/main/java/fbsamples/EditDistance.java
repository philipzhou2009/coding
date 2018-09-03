package fbsamples;

import lombok.extern.slf4j.Slf4j;

import static java.lang.Math.abs;

/**
 * Write a function to return if two words are exactly "one edit" away, where an edit is:
 * Inserting one character anywhere in the word (including at the beginning and end)
 * Removing one character
 * Replacing exactly one character
 */
@Slf4j
class EditDistance {

    static boolean solution(String word1, String word2) {

        log.info("solution");

        int word1Length = word1.length();
        int word2Length = word2.length();

        if (abs(word1Length - word2Length) > 1) {
            return false;
        }

        // replace
        if (word1Length == word2Length) {
            int counter = 0;

            for (int i = 0; i < word1Length; i++) {
                if (word1.charAt(i) != word2.charAt(i)) {
                    counter++;

                    if (counter > 1) {
                        return false;
                    }
                }
            }

            return true;
        }

        // insert case
        // remove case
        String sShort = word1;
        String sLong = word2;

        if (word1Length > word2Length) {
            sShort = word2;
            sLong = word1;
        }

        for (int i = 0; i < sLong.length(); i++) {
            String result = sLong.replaceFirst(Character.toString(sLong.charAt(i)), "");
            if (sShort.equals(result)) {
                return true;
            }
        }

        return false;
    }
}
