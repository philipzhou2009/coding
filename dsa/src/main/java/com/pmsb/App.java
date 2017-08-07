package com.pmsb;

import com.pmsb.Sorting.SortingAlgo;

/**
 * Hello world!
 *
 */
public class App {

    public static void main(String[] args) {
        System.out.println("Hello DSA!");

        SortingAlgo sa = SortingAlgo.QUICK;
        Sorting.sortingFactory(sa);
    }
}
