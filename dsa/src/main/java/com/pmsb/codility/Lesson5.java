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
        int[] A = {4, 2, 2, 5, 1, 5, 8};

        int result = MinAvgTwoSliceSolution(A);
        System.out.printf("MinAvgTwoSlice, result=%d\n", result);

    }

    private static int MinAvgTwoSliceSolution(int[] A) {
        int length = A.length;
        
        for(int i=0; i< length; i++)
        {
            
        }
        
        return 0;
    }
}
