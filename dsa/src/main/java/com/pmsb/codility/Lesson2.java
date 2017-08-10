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
public class Lesson2 {

    public static void CyclicRotation() {
        int[] A = {3, 8, 9, 7, 6};
        int K = 16;

        int[] result = CyclicRotationSolution(A, K);
        System.out.println(Arrays.toString(result));

    }

    public static int[] CyclicRotationSolution(int[] A, int K) {
        int length = A.length;
        int[] result = new int[length];

        for (int i = 0; i < length; i++) {
            int value = A[i];

            int newIdx = (i + K) % length;
            result[newIdx] = value;
        }

        return result;
    }

    public static void OddOccurrencesInArray() {
        int[] A = {9, 3, 9, 3, 9, 7, 9};

        int result = OddOccurrencesInArraySolution(A);
        System.out.println("OddOccurrencesInArray: array=" + Arrays.toString(A));
        System.out.println("OddOccurrencesInArray: result=" + result);
    }

    static int OddOccurrencesInArraySolution(int[] A) {
        int length = A.length;
        int result = 0;

        for(int i=0; i< length;i++)
        {
            int tmp = A[i];
            
            result ^= tmp;
        }
        
        return result;
    }
}
