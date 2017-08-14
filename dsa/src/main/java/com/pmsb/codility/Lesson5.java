/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.pmsb.codility;

import java.util.Arrays;
import com.pmsb.Utils;

/**
 *
 * @author philip
 */
public class Lesson5 {

    public static void PassingCars() {
        int[] A1 = {1};
        int[] A2 = {0, 1, 0, 1, 1};
        int[] A3 = Utils.ArrayGenerator(50, 0, 1);

        int result = PassingCarsSolution(A3);
        System.out.printf("PassingCars, result=%d\n", result);

    }

    private static int PassingCarsSolution(int[] A) {
        int length = A.length;

        int result = 0, value = 0;
        int count1 = 0;
        for (int i = length - 1; i >= 0; i--) {
            value = A[i];
            if (value == 0) {
                result += count1;
                if (result > 1000000000) {
                    return -1;
                }
            } else {
                count1++;
            }
        }

        return result;
    }

    public static void CountDiv() {

        int A = 0, B = 1, K = 11;
        int result = CountDivSolution(A, B, K);
        System.out.printf("CountDiv, result=%d\n", result);

    }

    private static int CountDivSolution(int A, int B, int K) {
        if (A == 0) {
            return B / K + 1;
        }

        if (B == 0) {
            return 1;
        }

        return B / K - (A - 1) / K;
    }

    public static void MinAvgTwoSlice() {

        int[] A;

        int choice = 2;
        switch (choice) {
            case 0:
                A = new int[]{4, 2, 2, 5, 1, 5, 8};
                break;
            case 1:
                A = Utils.ArrayGenerator(8, 0, 10);
                break;
            default:
                A = new int[]{0, 0, 0, 1};
                break;

        }
        System.out.println("Array=" + Arrays.toString(A));
        int result = MinAvgTwoSliceSolution(A);
        System.out.printf("MinAvgTwoSlice, result=%d\n", result);

    }

    private static int MinAvgTwoSliceSolution(int[] A) {
        int length = A.length;

        int c1 = 0, c2 = 0;
        int sum = A[0] + A[1];
        double avg = ((double) sum) / 2;
        double minAvg = avg;

        int sumTmp = 0;
        double avgTmp = 0;

        int i = 2, j = 0;
        int mc1 = c1, mc2 = c1 + 1;

        while (true) {
            c1 = c2;
            c2 = c1 + 1;

            if (c1 >= length || c2 >= length) {
                break;
            }

            sum = A[c1] + A[c2];
            avg = ((double) sum) / 2;
//            System.out.printf("start: c1=%d, c2=%d, avg=%f\n", c1, c2, avg);

            i = c2 + 1;
            while (i < length) {
                int valI = A[i];
                // c2 go down
                sumTmp = sum + valI;
                avgTmp = ((double) sumTmp) / (i - c1 + 1);

                if (avgTmp < avg) {
                    c2 = i;
                    sum = sumTmp;
                    avg = avgTmp;
                    mc2 = c2;

                    if (avg < minAvg) {
                        minAvg = avg;
                        mc1 = c1;
                    }
//                    System.out.printf("c2 drop: c1=%d, c2=%d, avg=%f\n", c1, c2, avg);

                    i++;

                } else {
                    break;
                }
            }

            // c2 stop, c1 down
            for (j = c1; j < c2 - 1; j++) {
                int valJ = A[j];
                int sumTmpJ = sum - valJ;
                double avgJ = ((double) sumTmpJ) / (c2 - j);
//                    System.out.printf("c1 drop: j=%d, sumTmpJ=%d, avg=%f\n", j, sumTmpJ, avgJ);

                if (avgJ >= avg) {
                    break;
                } else {
                    c1 = j + 1;
                    sum = sumTmpJ;
                    avg = avgJ;
                }
            }

            // c1 also stop
            if (avg < minAvg) {
                minAvg = avg;
                mc1 = c1;
            }

//            System.out.printf("done: c1=%d, c2=%d, avg=%f, minAvg=%f, mc1=%d\n", c1, c2, avg, minAvg, mc1);
        }

        return mc1;
    }

    public static void GenomicRangeQuery() {
        int[] P = {2, 5, 0, 5, 11};
        int[] Q = {4, 5, 6, 10, 20};
        String S = "CAGCCTAGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG";

        int[] result;
        Utils.timerStart();
        result = GenomicRangeQuerySolution0(S, P, Q);
        Utils.timerOutput();
        System.out.printf("GenomicRangeQuery, result0=%s\n", Arrays.toString(result));

        Utils.timerStart();
        result = GenomicRangeQuerySolution1(S, P, Q);
        Utils.timerOutput();
        System.out.printf("GenomicRangeQuery, result1=%s\n", Arrays.toString(result));

        Utils.timerStart();
        result = GenomicRangeQuerySolution2(S, P, Q);
        Utils.timerOutput();
        System.out.printf("GenomicRangeQuery, result2=%s\n", Arrays.toString(result));
    }

    private static int[] GenomicRangeQuerySolution0(String S, int[] P, int[] Q) {
        int length = P.length;

        int sLen = S.length();
        int[] sArray = new int[sLen];
        for (int i = 0; i < sLen; i++) {
            char c = S.charAt(i);
            if (c == 'A') {
                sArray[i] = 1;
            }

            if (c == 'C') {
                sArray[i] = 2;
            }

            if (c == 'G') {
                sArray[i] = 3;
            }

            if (c == 'T') {
                sArray[i] = 4;
            }

        }

//        char[] chs = S.toCharArray();
        int[] result = new int[length];

        char[] acgt = {'A', 'C', 'G', 'T'};
        int i, j, k, tmp1, tmp2, min = 0;
        int piv = 1;
        for (i = 0; i < length; i++) {
//            str = S.substring(P[i], Q[i] + 1);
//            System.out.println("sub str=" + str);
            tmp1 = P[i];
            tmp2 = Q[i];
            min = 0;
            for (j = tmp1; j <= tmp2; j++) {
                min = (min == 0 || sArray[j] < min) ? sArray[j] : min;
            }

            result[i] = min;
        }

        return result;
    }

    private static int[] GenomicRangeQuerySolution1(String S, int[] P, int[] Q) {
        int length = P.length;

        int sLen = S.length();
        int[] sArray = new int[sLen];
        for (int i = 0; i < sLen; i++) {
            char c = S.charAt(i);
            if (c == 'A') {
                sArray[i] = 1;
            }

            if (c == 'C') {
                sArray[i] = 2;
            }

            if (c == 'G') {
                sArray[i] = 3;
            }

            if (c == 'T') {
                sArray[i] = 4;
            }

        }

        int[] result = new int[length];

        int i, k, tmp1, tmp2, min = 0;
        boolean found = false;
        for (i = 0; i < length; i++) {
            tmp1 = P[i];
            tmp2 = Q[i];
            min = 0;

            for (k = 0; k < i; k++) {
                if (P[k] >= tmp1 && Q[k] <= tmp2) {
                    min = result[k];

                    if (min != 1) {
                        int minLeft = findMin(sArray, tmp1, P[k]);
                        int minRight = findMin(sArray, Q[k], tmp2);

                        min = min < minLeft ? min : minLeft;
                        min = min < minRight ? min : minRight;
                    }
                    found = true;

                    break;
                }

            }

            if (!found) {
                min = findMin(sArray, tmp1, tmp2);
            }

            found = false;
            result[i] = min;
        }

        return result;
    }

    private static int findMin(int[] sArray, int left, int right) {
        int min = 0;
        for (int j = left; j <= right; j++) {
            min = (min == 0 || sArray[j] < min) ? sArray[j] : min;
        }

        return min;
    }

    private static int[] GenomicRangeQuerySolution2(String S, int[] P, int[] Q) {
        int length = P.length;

        int sLen = S.length();
        int[] sArray = new int[sLen];
        for (int i = 0; i < sLen; i++) {
            char c = S.charAt(i);
            if (c == 'A') {
                sArray[i] = 1;
            }

            if (c == 'C') {
                sArray[i] = 2;
            }

            if (c == 'G') {
                sArray[i] = 4;
            }

            if (c == 'T') {
                sArray[i] = 8;
            }

        }

        int[] result = new int[length];

        int i, k, tmp1, tmp2, min = 0, minLeft = 0, minRight;
        boolean found = false;
        for (i = 0; i < length; i++) {
            tmp1 = P[i];
            tmp2 = Q[i];
            min = 0;

            for (k = 0; k < i; k++) {
                if (P[k] >= tmp1 && Q[k] <= tmp2) {
                    min = result[k];

                    if (min != 1) {
                        minLeft = findMin2(sArray, tmp1, P[k]);
                        min = min < minLeft ? min : minLeft;

                        if (min != 1) {
                            minRight = findMin2(sArray, Q[k], tmp2);
                            min = min < minRight ? min : minRight;
                        }
                    }
                    found = true;

                    break;
                }

            }

            if (!found) {
                min = findMin2(sArray, tmp1, tmp2);
            }

            found = false;
            result[i] = min;
        }

        return result;
    }

    private static int findMin2(int[] sArray, int left, int right) {
        int min = 0;
        for (int j = left; j <= right; j++) {
            min |= sArray[j];
        }

        if ((min & 1) == 1) {
            return 1;
        }

        if ((min & 2) == 2) {
            return 2;
        }

        if ((min & 4) == 4) {
            return 3;
        }

        return 4;
    }

}
