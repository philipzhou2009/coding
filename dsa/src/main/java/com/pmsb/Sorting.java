package com.pmsb;

import java.util.Arrays;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;

public class Sorting {
    public enum SortingAlgo {
        BUBBLE, INSERTION, SELECTION, MERGE, SHELL, QUICK
    };

    public static void sortingFactory(SortingAlgo sa) {
        int length = 15;
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
            case SHELL:
                result = shellSort(A);
                break;
            case QUICK:
                quickSort(A);
                break;
            default:
                result = new int[1];
                System.out.println("No algo selected");
                break;
        }

        System.out.printf(format, "After Sorting:", Arrays.toString(A));

        int last = A[0];
        boolean success = true;
        for (int i = 1; i < length; i++) {
            if (A[i] < last) {
                success = false;
            }
            last = A[i];
        }

        if (success) {
            System.out.printf(format, "Sorting Success", new int[0]);
        } else {
            System.out.printf(format, "Sorting Failed", new int[0]);
        }
    }

//     quite efficient for large-sized data sets as its average and worst case complexity are of Ο(n2),
    static void quickSort(int[] A) {
        int length = A.length;
        paritionSort(A, 0, length - 1);
    }

    static void paritionSort(int[] A, int first, int last) {
//        System.out.println(Arrays.toString(A));

        if (first >= last) {
            return;
        }

        int pivot = A[last];

        int i = first, j = last - 1;
        while (true) {

            if (i >= j) {
                if (A[i] > pivot) {
                    int tmp = A[i];
                    A[i] = pivot;
                    A[last] = tmp;

                    paritionSort(A, first, i - 1);
                    paritionSort(A, i + 1, last);
                } else {
                    paritionSort(A, first, i);
                    paritionSort(A, i + 1, last);
                }
                break;
            }

            int left = A[i], right = A[j];
            if (left > pivot && right < pivot) {
                A[i] = right;
                A[j] = left;

                i++;
                j--;
            }

            if (left <= pivot) {
                i++;
            }

            if (right >= pivot) {
                j--;
            }

        }
    }

    // average and worst case complexity are of Ο(n)
    static int[] shellSort(int[] A) {
        int length = A.length;

        int interval = 1;
        while (interval < length / 3) {
            interval = interval * 3 + 1;
        }

        // 13->4->1
        while (interval > 0) {
            for (int i = 0; i < interval; i++) {

                for (int j = i; j < length; j += interval) {

                    for (int k = i; k < j; k += interval) {
                        if (A[k] > A[j]) {
                            int tmp = A[j];
                            A[j] = A[k];
                            A[k] = tmp;
                        }
                    }
                }
            }

            interval = (interval - 1) / 3;
        }

        return A;
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
