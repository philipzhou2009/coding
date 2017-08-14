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

        int result;
        result = TriangleSolution(A);
        System.out.printf("Triangle, result=%d\n", result);

    }

    private static int TriangleSolution(int[] A) {
        int length = A.length;
        
        
        
        return 0;
    }

    public static void NumberOfDiscIntersections() {
    }

    private static int NumberOfDiscIntersectionsSolution(int[] A) {
        return 0;
    }

}
