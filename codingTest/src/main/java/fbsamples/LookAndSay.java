package fbsamples;

import lombok.extern.slf4j.Slf4j;

/**
 * Implement a function that outputs the Look and Say sequence:
 * 1
 * 11
 * 21
 * 1211
 * 111221
 * 312211
 * 13112221
 * 1113213211
 * 31131211131221
 * 13211311123113112211
 */

@Slf4j
public class LookAndSay {


    public static void print_look_and_say_seq(int count) {
        int val = 1;
        for (int i = 1; i <= count; i++) {

            log.info("" + val);
            String s = output_val(val);
            val = Integer.parseInt(s);
        }
    }

    public static String output_val(int val) {
        String input = "" + val;
        if (input.length() == 1) {
            return "1" + input;
        }

        String ret = "";
        char cur = input.charAt(0);
        int count = 1;
        for (int i = 1; i <= input.length(); i++) {
            if (cur != input.charAt(i) || i == input.length()) {
                ret += "" + count + cur;
                count = 1;
                cur = input.charAt(i);
            } else {
                count++;
            }
        }
        return ret;
    }
}
