/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.pmsb;

//import com.google.common.base.Stopwatch;
import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

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

    public static int[] ArrayGenerator(int length, int min, int max) {
        int[] array = new int[length];
        for (int i = 0; i < length; i++) {
            array[i] = ThreadLocalRandom.current().nextInt(min, max + 1);
        }
//        System.out.println("ArrayGenerator=" + Arrays.toString(array));
        return array;
    }

    public static void OutputResult(String name, int result) {
        System.out.printf("%s, result=%d\n", name, result);

    }

}
