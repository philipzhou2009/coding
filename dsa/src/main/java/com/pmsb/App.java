package com.pmsb;

import com.pmsb.Sorting.SortingAlgo;
import com.pmsb.codility.Codility;
import static com.pmsb.codility.Codility.lessons;
import com.pmsb.testdome.Testdome;
import static com.pmsb.testdome.Testdome.Question;
/**
 * Hello world!
 *
 */
public class App {

    static enum Test {
        Sorting, Codility, Testdome
    };

    public static void main(String[] args) {
        System.out.println("Hello DSA!");

        Test test = Test.Testdome;

        switch (test) {
            case Sorting:
                SortingAlgo sa = SortingAlgo.QUICK;
                Sorting.sortingFactory(sa);
                break;
            case Codility:
                lessons lesson = lessons.CL64;
                Codility.lessonFactory(lesson);
                break;
            case Testdome:
                Question q = Question.TrainComposition;
                Testdome.QFactory(q);
            default:
                break;

        }
    }
}
