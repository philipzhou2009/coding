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
public class Lesson1 {

    public static int solution(int N) {

        int gap = -1;
        int max = -1;
        int last = N;
        while (true) {

            int tmp1 = last % 2;
//            System.out.print(tmp1);

            if (tmp1 == 1) {

                if (gap == -1) { // first appear
                    gap++;
                    max = gap > max ? gap : max;

                } else { // re-calc
                    max = gap > max ? gap : max;
                    gap = 0;
                }

            } else { // continue
                if (gap >= 0) {
                    gap++;
                }
            }

            last = (int) (last / 2);

            if (last <= 0) {
                break;
            }
        }

        System.out.printf("Lesson 1: iNumber=%d, Result=%d\n", N, max);
        return max;
    }
}
