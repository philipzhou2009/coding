/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package codility01;

import java.util.*;

/**
 *
 * @author philip
 */
public class lesson8 {

    void runDominator() {
        int[] A = {3, 4, 3, 2, 3, -1};
        int[] A1 = {3, 4, 3, 3, 3, -1};

        System.out.println(Dominator(A1));
    }

    int Dominator(int[] A) {
        int length = A.length;
        int halfLength = length / 2;

        Map<Integer, Integer> m = new HashMap<>();

        int i = 0;
        int key = 0;
        int counter = 0;
        for (; i < length; i++) {
            key = A[i];
            if (m.containsKey(key)) {
                m.put(key, m.get(key) + 1);
            } else {
                m.put(key, 1);
            }

            if (m.get(key) > counter) {
                counter = m.get(key);

                if (counter > halfLength) {
                    return i;
                }
            }
        }

        return -1;
    }

    void runEquiLeader() {
        int[] A = {4, 3, 4, 4, 4, 2};
        int[] A1 = {4};
        System.out.println(EquiLeader(A));
    }

    int EquiLeader(int[] A) {
        int length = A.length;
        int halfLength = length / 2;

        Map<Integer, Integer> m = new HashMap<>();

        int i = 0;
        int key = 0;
        int counter = 0;
        int leader = 0;
        boolean found = false;
        for (; i < length; i++) {
            key = A[i];
            if (m.containsKey(key)) {
                m.put(key, m.get(key) + 1);
            } else {
                m.put(key, 1);
            }

            if (m.get(key) > counter) {
                counter = m.get(key);

                if (counter > halfLength) {
                    leader = key;
                    found = true;
                }
            }
        }

        if (!found) {
            return 0;
        }

        //System.out.println("leader counter="+counter);
        int counter1 = 0;
        int counter2 = 0;
        for (i = 0; i < length; i++) {
            int half1 = (i + 1) / 2;
            int half2 = (length - i - 1) / 2;

            int tmp = A[i];
            if (tmp == leader) {
                counter1++;
            }

            if (counter1 > half1 && (counter - counter1) > half2) {
                counter2++;
            }
        }

        return counter2;
    }
}
