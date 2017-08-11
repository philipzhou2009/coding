/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.pmsb.codility;

import java.util.Arrays;

/**
 *
 * @author philip
 */
public class Lesson4 {

    public static void MissingInteger() {
        int[] A1 = {1, 3, 6, 4, 1, 2};
        int[] A2 = {1, 2, 3};
        int[] A3 = {-1, 13};

        int result = MissingIntegerSolution(A1);

        System.out.println("Lesson4:MissingInteger, result=" + result);
    }

    private static int MissingIntegerSolution(int[] A) {
        int length = A.length;

        int[] B = new int[length];
        int result = 1;
        for (int i = 0; i < length; i++) {
            int value = A[i];
            if (value > 0 && value < length + 1) {
                B[value - 1] = 1;
            }
        }

        System.out.println("B=" + Arrays.toString(B));
        boolean found = false;
        for (int j = 0; j < length; j++) {
            if (B[j] == 0) {
                result = j + 1;
                found = true;
                break;
            }
        }
        result = found ? result : length + 1;

        return result;
    }

    public static void PermCheck() {
        int[] A1 = {4, 1, 3, 2};
        int[] A2 = {4, 1, 3, 3, 2, 5, 6, 6};

        int result = PermCheckSolution(A2);

        System.out.println("Lesson4:PermCheckSolution, result=" + result);
    }

    private static int PermCheckSolution(int[] A) {
        int length = A.length;

        int B = (1 << length) - 1;
        int value;
        int flag = 0;
        for (int i = 0; i < length; i++) {
            value = A[i];
            if (value > length) {
                return 0;
            }

            flag |= 1 << (value - 1);
        }

//        System.out.printf("Lesson4:PermCheckSolution, B=%s, flag=%s\n", Integer.toBinaryString(B), Integer.toBinaryString(flag));
        if (B != flag) {
            return 0;
        }

        return 1;
    }

    public static void FrogRiverOne() {
        int[] A1 = {1, 3, 1, 4, 2, 3, 5, 4};

        int[] A2 = new int[150];
        for (int i = 0; i < 150; i++) {
            A2[i] = i + 1;
        }

        int result = FrogRiverOneSolution(5, A1);

        System.out.println("Lesson4:FrogRiverOne, result=" + result);

    }

    private static int FrogRiverOneSolution(int X, int[] A) {
        int length = A.length;

        int size = 10;
        // X to array
        int xLen = ((X % 10) > 0) ? (X / 10) + 1 : (X / 10);
        int[] B = new int[xLen];

        int val1 = (1 << 10) - 1;
        int val2 = ((X % 10) > 0) ? (1 << (X % 10)) - 1 : val1;

//        System.out.printf("val1=%d, val2=%d\n", val1, val2);
        int result = -1;
        int value = 0;
        int dist, idx1, idx2 = 0;
        boolean eq = true;
        for (int i = 0; i < length; i++) {
            value = A[i];
            if (value > X) {
                continue;
            }

            dist = value - 1;
            idx1 = xLen - (dist / 10) - 1;
            idx2 = dist % 10;
//            System.out.printf("value=%d, idx1=%d, idx2=%d\n", value, idx1, idx2);

            B[idx1] |= 1 << idx2;

            eq = true;

            for (int j = 0; j < xLen; j++) {
                if (j == xLen - 1) {
                    if (val2 != B[j]) {
                        eq = false;
                        break;
                    }
                } else if (val1 != B[j]) {
                    eq = false;
                    break;
                }
            }

            if (eq) {
                result = i;
                break;
            }
        }

//        for (int k = 0; k < xLen; k++) {
//            System.out.printf("Lesson4:FrogRiverOneSolution, B=%s\n",
//                    Integer.toBinaryString(B[k]));
//        }
        return result;
    }

    public static void MaxCounters() {
        int[] A = {3, 4, 4, 6, 1, 4, 4};
        
        int N = 5;
        
        int[] result = MaxCountersSolution(N, A);
        
        System.out.println("MaxCounters, result="+ Arrays.toString(result));
    }

    private static int[] MaxCountersSolution(int N, int[] A) {

    }
}
