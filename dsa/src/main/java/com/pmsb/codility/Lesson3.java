/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.pmsb.codility;

/**
 *
 * @author philip
 */
public class Lesson3 {

    public static void PermMissingElem() {
        int[] A = {2, 3, 1, 5};

        int result = PermMissingElemSolution(A);

        System.out.println("Lesson3:PermMissingElem, result=" + result);
    }

    static int PermMissingElemSolution(int[] A) {
        int length = A.length;

        int sum = 0, sum1 = 0;

        for (int i = 0; i < length; i++) {
            sum += A[i];
            sum1 += i + 1;
        }

        sum1 += length + 1;

        return sum1 - sum;
    }

    public static void FrogJmp() {
        int X = 10, Y = 85, D = 30;
        int result = FrogJmpSolution(X, Y, D);
        System.out.println("Lesson3:FrogJmp, result=" + result);

    }

    static int FrogJmpSolution(int X, int Y, int D) {
        int distance = Y - X;

        int result = distance % D > 0 ? (int) (distance / D) + 1 : (distance / D);

        return result;

    }

    public static void TapeEquilibrium() {
        int[] A = {3, 1, 2, 4, 3};
        int result = TapeEquilibriumSolution(A);

        System.out.println("Lesson3:TapeEquilibrium, result=" + result);

    }

    private static int TapeEquilibriumSolution(int[] A) {
        int length = A.length;

        int sum = 0;
        for (int i = 0; i < length; i++) {
            sum += A[i];
        }

        int sumPart1 = 0, sumPart2 = 0;
        int min = -1, diff = 0;
        for (int j = 0; j < length - 1; j++) {
            sumPart1 += A[j];
            sumPart2 = sum - sumPart1;

            diff = Math.abs(sumPart2 - sumPart1);
            min = (diff < min || min == -1) ? diff : min;
        }

        return min;

    }

}
