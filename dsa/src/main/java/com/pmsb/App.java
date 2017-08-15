package com.pmsb;

import com.pmsb.Sorting.SortingAlgo;
import com.pmsb.codility.Codility;
import static com.pmsb.codility.Codility.lessons;

/**
 * Hello world!
 *
 */
public class App {

    static enum Test {
        Sorting, Codility
    };

    public static void main(String[] args) {
        System.out.println("Hello DSA!");

        Test test = Test.Codility;

        switch (test) {
            case Sorting:
                SortingAlgo sa = SortingAlgo.QUICK;
                Sorting.sortingFactory(sa);
                break;
            case Codility:
                lessons lesson = lessons.CL64;
                Codility.lessonFactory(lesson);
                break;

            default:
                break;

        }
    }
}
