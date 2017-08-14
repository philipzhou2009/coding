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
}
