/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.pmsb.codility;

import com.pmsb.Utils;
import java.util.Arrays;

/**
 *
 * @author philip
 */
public class Lesson6 {

    public static void Distinct() {
        int[] A = Utils.ArrayGenerator(0, 0, 5);
        int result;

        System.out.printf("Distinct, input=%s\n", Arrays.toString(A));
        result = DistinctSolution(A);
        System.out.printf("Distinct, result=%d\n", result);

    }

    private static int DistinctSolution(int[] A) {
        int length = A.length;
        if (length == 0) {
            return 0;
        }

        Arrays.sort(A);

        int last = A[0];
        int result = 1;
        for (int i = 1; i < length; i++) {
            if (A[i] != last) {
                result++;
                last = A[i];
            }

        }
        return result;
    }

    public static void MaxProductOfThree() {
    }

    private static int MaxProductOfThreeSolution(int[] A) {
        return 0;
    }

    public static void Triangle() {
        int[] A = {10, 2, 5, 1, 8, 20};
        int[] A1 = {10, 50, 5, 1};
        int[] A2 = {-10, -8, -5};
        int result;
        result = TriangleSolution(A1);
        System.out.printf("Triangle, result=%d\n", result);

    }

    private static int TriangleSolution(int[] A) {
        int length = A.length;

        if (length < 3) {
            return 0;
        }

        Arrays.sort(A);

        int c2 = (length / 2), c1, c3;
        int n1, n2, n3;
        boolean result = false;

        while (true) {
            c1 = c2 - 1;
            c3 = c2 + 1;

            if (c1 < 0) {
                break;
            }

            n1 = A[c1];
            n2 = A[c2];
            n3 = A[c3];

            result = TriangleCheck(n1, n2, n3);

            if (result) {
                return 1;
            }

            c2 -= 1;
        }

        c2 = (length / 2);

        while (true) {
            c1 = c2 - 1;
            c3 = c2 + 1;

            if (c3 >= length) {
                break;
            }

            n1 = A[c1];
            n2 = A[c2];
            n3 = A[c3];

            result = TriangleCheck(n1, n2, n3);

            if (result) {
                return 1;
            }

            c2 += 1;
        }

        return 0;
    }

    private static boolean TriangleCheck0(int n1, int n2, int n3) {
        if ((n1 + n2 > n3) & (n1 + n3 > n2) & (n2 + n3 > n1)) {
            return true;
        }
        return false;
    }

    private static boolean TriangleCheck(int n1, int n2, int n3) {
        long x1 = (long) n1;
        long x2 = (long) n2;
        long x3 = (long) n3;

        if ((x1 + x2 > x3) & (x1 + x3 > x2) & (x2 + x3 > x1)) {
            return true;
        }
        return false;
    }

    public static void NumberOfDiscIntersections() {
        int[] A = {1, 5, 2, 1, 4, 0};

        int result;
        result = NumberOfDiscIntersectionsSolution(A);
        Utils.OutputResult("NumberOfDiscIntersections", result);

    }

    private static int NumberOfDiscIntersectionsSolution(int[] A) {
        int length = A.length;

        int n1, n2;
        int x1, x2;
        int val, tmp1, result = 0;
        for (int i = 0; i < length; i++) {
            val = A[i];
            n1 = i - val;
            n2 = i + val;

            for (int j = i + 1; j < length; j++) {
                tmp1 = A[j];
                x1 = j - tmp1;
                x2 = j + tmp1;

                if ((x1 <= n1 && n1 <= x2) || (x1 <= n2 && n2 <= x2) || (n1 <= x1 && n2 >= x2)) {
                    result++;
                }
            }

        }

        result = result > 10000000 ? -1 : result;

        return result;
    }

}
