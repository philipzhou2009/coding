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
public class lesson7 {

    void runFish() {
        int[] A = {4, 3, 2, 1, 5};
        int[] B1 = {1, 1, 1, 1, 0}; // 1
        int[] B2 = {0, 1, 0, 0, 0}; //2

        int[] B3 = {1, 0, 1, 0, 1}; //3
        int[] B4 = {1, 1, 1, 0, 1}; //4 

        int[] B5 = {1, 1, 0, 0, 1}; //3
        System.out.println(Fish(A, B5));
    }

    public int Fish(int[] A, int[] B) {

        int length = A.length;
        if (length == 1) {
            return 1;
        }

        int f1size = 0, f2size = 0, f1dir = 0, f2dir = 0;
        int f1idx = 0, f2idx = 1;
        int counter = length;

        while (true) {
            if (f2idx >= length) {
                break;
            }

            if (f1idx < 0) {
                f1idx = f2idx;
                f2idx++;
                continue;
            }

            f1size = A[f1idx];
            f2size = A[f2idx];

            f1dir = B[f1idx];
            f2dir = B[f2idx];

            if (f1dir <= f2dir) {
                f1idx = f2idx;
                f2idx++;
                continue;
            } else {
                if (f1size > f2size) {
                    f2idx++;
                } else {
                    f1idx--;
                }

                counter--;
            }
        }

        return counter;
    }
}
