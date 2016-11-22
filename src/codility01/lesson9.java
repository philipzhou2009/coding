/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package codility01;

/**
 *
 * @author philip
 */
public class lesson9 {

    void runMaxSliceSum() {
        int[] A = {-3, -2};
        int[] A1 = {3, 2, -6, 4, 0};
        System.out.println(MaxSliceSum(A1));
    }

    int MaxSliceSum(int[] A) {

        int length = A.length;
        if (length == 1) {
            return A[0];
        }

        int max_ending = A[0], max_slice = A[0];

        int i = 1;
        for (; i < length; i++) {
            max_ending = Math.max(A[i], max_ending + A[i]);
            max_slice = Math.max(max_slice, max_ending);
        }

        return max_slice;
    }

    void runMaxDoubleSliceSum() {
        int[] A = {3, 2, 6, -1, 4, 5, -1, 2}; // 0, 6
        int[] A1 = {0, 0, 0, 1, 1, -10000, 1}; // 0, 5
        int[] A2 = {-1, -2, -3, 1, 1, 10000, 1}; // 2,6
        int[] A3 = {1, 1, 1, -1, -1, -1};// 0, 3
        
        int[] A4 = {-1, -1, 1, -1, -1, -1}; //1,3

        System.out.println(MaxDoubleSliceSum(A3));

    }

    int MaxDoubleSliceSum(int[] A) {

        int length = A.length;
        if (length == 3) {
            return 0;
        }

        int max_ending = A[1], max_slice = A[1];
        int left = 0, right = 2;

        int i = 3;
        for (; i < length; i++) {
            //max_ending = Math.max(A[i - 1], max_ending + A[i - 1]);
            if (A[i - 1] > max_ending + A[i - 1]) {
                max_ending = A[i - 1];
                left = i - 2;
            } else {
                max_ending = max_ending + A[i - 1];
            }

            //max_slice = Math.max(max_slice, max_ending);
            if (max_slice < max_ending) {
                max_slice = max_ending;
                right = i;
            }
        }

        System.out.println("left=" + left + ",right=" + right + ",max_slice=" + max_slice);

        int min = A[left + 1];
        for (i = left + 1; i < right; i++) {
            min = Math.min(min, A[i]);
        }

        max_slice -= min;

        return max_slice;
    }
}
