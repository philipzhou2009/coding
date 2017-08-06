/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package DSA;

import DSA.algorithm.Sorting;
import DSA.algorithm.Sorting.SortingAlgo;
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
                
        SortingAlgo sa = SortingAlgo.MERGE;  
        Sorting.sortingFactory(sa);
        
//        switch (i) {
//            case 0:
////                int[] result = Sorting.bubbleSort();
////                System.out.println(Arrays.toString(result));
//                Sorting.sortingFactory();
//                break;
//
//            default:
//                System.out.println("no feature selected");
//                break;
//        }
    }

}
