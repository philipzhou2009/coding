package codesignal;

import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.Set;

public class CountPairsWithSum {

    int countPairsWithSum(int k, int[] a) {

        Arrays.sort(a);

        int len = a.length;
        int cursor = 0;
        int cursorR = 1;
        int result = 0;

        while (cursor < len) {
            int i = a[cursor];
            while (cursorR < len) {
                int j = a[cursorR++];
                if (i + j == k) {
                    System.out.println("found!" + i + "," + j);
                    result++;
                    break;
                }
            }

            do {
                cursor++;
            } while (cursor < len && a[cursor] == i);

            cursorR = cursor + 1;

            if (i > k / 2) {
                break;
            }
        }

        return result;
    }


    int countPairsWithSum0(int k, int[] a) {

        Set<Integer> distSet = new LinkedHashSet<>();

        int len = a.length;
        int cursor = 0;
        int cursorR = 1;
        int result = 0;

        while (cursor < len) {
//            System.out.println("cursor=" + cursor + ",cursorR=" + cursorR);
            int i = a[cursor];
            while (cursorR < len) {
                int j = a[cursorR++];
                if (i + j == k) {
                    System.out.println("found!" + i + "," + j);
                    if (distSet.contains(i)) {
                        break;
                    } else {
                        distSet.add(i);
                        distSet.add(j);
                        result++;
                    }
                }
            }
//            System.out.println("xx::cursor=" + cursor + ",cursorR=" + cursorR);
            do {
                cursor++;
            } while (cursor < len && a[cursor] == i);

            cursorR = cursor + 1;
        }

        return result;
    }
}
