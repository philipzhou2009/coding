/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package DSA;

import DSA.algorithm.Sorting;
import java.util.Arrays;

/**
 *
 * @author philip
 */
public class JavaApplication {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

        int i = 0;
        int[] sortingArr = {20, 0, 19, 9, 18, 8, 12, 2};
        
        switch (i) {
            case 0:
                int[] result = Sorting.bubbleSort(sortingArr);
                System.out.println(Arrays.toString(result));
                break;

            default:
                System.out.println("no feature selected");
                break;
        }
    }

}
