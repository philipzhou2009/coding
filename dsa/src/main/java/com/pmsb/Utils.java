/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.pmsb;

/**
 *
 * @author philip
 */
public class Utils {

    private static long startTime;
    private static long stopTime;

    public static void timerStart() {
        startTime = System.nanoTime();
        stopTime = 0;
    }

    public static void timerOutput() {
        stopTime = System.nanoTime();
        System.out.printf("Running Time=%d, start=%d, stop=%d\n", 
                stopTime - startTime, startTime, stopTime);
        startTime = stopTime;
    }

}