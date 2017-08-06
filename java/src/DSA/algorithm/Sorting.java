package DSA.algorithm;

import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

public class Sorting {

    public enum SortingAlgo {
        BUBBLE, INSERTION, QUICK
    };

    static int[] A = {20, 0, 19, 9, 18, 8, 12, 2};

    public static void sortingFactory(SortingAlgo sa) {
        int length = 10;
        int[] A = new int[length];
        int min = 1, max = 100;

        for (int i = 0; i < length; i++) {
            A[i] = ThreadLocalRandom.current().nextInt(min, max + 1);
        }

        String format = "%15s %s\n";
        System.out.printf(format, "Sorting By:", sa);
        System.out.printf(format, "Before Sorting:", Arrays.toString(A));
        int[] result;
        switch (sa) {
            case BUBBLE:
                result = bubbleSort(A);
                break;
            case INSERTION:
                result = insertionSort(A);
                break;
            default:
                result = null;
                break;
        }

        System.out.printf(format, "After Sorting:", Arrays.toString(A));
    }

    public static int[] insertionSort(int[] A) {
        int length = A.length;

        for (int i = 0; i < length - 1; i++) {
            boolean swapped = false;
            int j = i + 1;
            if (A[i] > A[j]) {
                int tmp = A[j];
                A[j] = A[i];
                A[i] = tmp;
                swapped = true;
            }

            if (swapped) {
                for (int k = 0; k < i; k++) {
                    if (A[k] > A[i]) {
                        int tmp = A[k];
                        A[k] = A[i];
                        A[i] = tmp;
                    }
                }
            }

        }

        return A;
    }

    public static int[] bubbleSort(int[] A) {
        int length = A.length;

        for (int j = length; j > 0; j--) {
            boolean swapped = false;
            for (int i = 0; i < j - 1; i++) {
                if (A[i] > A[i + 1]) {
                    int tmp = A[i + 1];
                    A[i + 1] = A[i];
                    A[i] = tmp;
                    swapped = true;
                }
            }

            if (!swapped) {
                break;
            }
        }

        return A;
    }
}
