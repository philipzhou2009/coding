/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.pmsb.codility;

import java.util.concurrent.ThreadLocalRandom;

/**
 *
 * @author philip
 */
public class Codility {

    public enum lessons {
        CL1, CL21, CL22, CL31, CL32, CL33, CL41, CL42, CL43, CL44,
        CL51, CL52, CL53, CL54, CL61, CL62, CL63, CL64
    };

    public static void lessonFactory(lessons lesson) {

        boolean condition = true;
        int iNumber = 15; //ranNumber();
//        int result = 0;

        switch (lesson) {
            case CL1:
                Lesson1.solution(iNumber);
                break;
            case CL21:
                Lesson2.CyclicRotation();
                break;
            case CL22:
                Lesson2.OddOccurrencesInArray();
                break;
            case CL31:
                Lesson3.PermMissingElem();
                break;
            case CL32:
                Lesson3.FrogJmp();
                break;
            case CL33:
                Lesson3.TapeEquilibrium();
                break;
            case CL41:
                Lesson4.MissingInteger();
                break;
            case CL42:
                Lesson4.PermCheck();
                break;
            case CL43:
                Lesson4.FrogRiverOne();
                break;
            case CL44:
                Lesson4.MaxCounters();
                break;
            case CL51:
                Lesson5.PassingCars();
                break;
            case CL52:
                Lesson5.CountDiv();
                break;
            case CL53:
                Lesson5.MinAvgTwoSlice();
                break;
            case CL54:
                Lesson5.GenomicRangeQuery();
                break;
            case CL61:
                Lesson6.Distinct();
                break;
            case CL62:
                Lesson6.MaxProductOfThree();
                break;
            case CL63:
                Lesson6.Triangle();
                break;
            case CL64:
                Lesson6.NumberOfDiscIntersections();
                break;                

            default:
                condition = false;
                break;
        }

        if (condition) {
//            
        } else {
            System.out.println("No Lesson Appointed");
        }

    }

    public static int ranNumber() {
        int min = 1, max = 10000;
        int iNumber = ThreadLocalRandom.current().nextInt(min, max + 1);
        return iNumber;

    }
}
