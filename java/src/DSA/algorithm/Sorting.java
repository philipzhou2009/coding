package DSA.algorithm;

import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

public class Sorting {

    public enum SortingAlgo {
        BUBBLE, INSERTION, SELECTION, MERGE, QUICK
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
            case SELECTION:
                result = selectionSort(A);
                break;
            case MERGE:
                result = mergeSort(A);
                break;
            default:
                result = new int[1];
                System.out.println("No algo selected");
                break;
        }

        System.out.printf(format, "After Sorting:", Arrays.toString(result));
    }

    // O(n log n)
    public static int[] mergeSort(int[] A) {
        int length = A.length;
        if (length == 1) {
            return A;
        }

        int half = length / 2;
        int[] left = Arrays.copyOfRange(A, 0, half);
        int[] right = Arrays.copyOfRange(A, half, length);

        left = mergeSort(left);
        right = mergeSort(right);

        return merge(left, right);
    }

    static int[] merge(int[] left, int[] right) {
        int leftLen = left.length, rightLen = right.length;
        int[] A = new int[leftLen + rightLen];

        int last = left[0], leftC = 0, rightC = 0, i = 0;
        while (true) {
            int leftOne = left[leftC];
            int rightOne = right[rightC];
            if (leftOne < rightOne) {
                A[i] = leftOne;
                leftC++;
            } else {
                A[i] = rightOne;
                rightC++;
            }

            i++;
            if (leftC >= leftLen || rightC >= rightLen) {
                break;
            }
        }

        if (leftC < leftLen) {
            while (leftC < leftLen) {
                A[i++] = left[leftC++];
            }
        } else {
            while (rightC < rightLen) {
                A[i++] = right[rightC++];
            }

        }

        return A;
    }

    public static int[] selectionSort(int[] A) {
        int length = A.length;

        for (int i = 0; i < length - 1; i++) {
            int min = A[i + 1];
            int pos = i + 1;

            for (int j = i + 2; j < length; j++) {
                if (A[j] < min) {
                    min = A[j];
                    pos = j;
                }
            }

            if (min < A[i]) {
                A[pos] = A[i];
                A[i] = min;
            }
        }

        return A;
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
