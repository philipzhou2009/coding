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
        CL1, CL21, CL22
    };

    public static void lessonFactory(lessons lesson) {

        boolean condition = false;
        int iNumber =15; //ranNumber();
//        int result = 0;
        
        switch (lesson) {
            case CL1:
                Lesson1.solution(iNumber);
                condition = true;
                break;
            case CL21:
                Lesson2.CyclicRotation();
                condition = true;
                break;
            case CL22:
                Lesson2.OddOccurrencesInArray();
                condition = true;
                break;                
            default:
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
