/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.pmsb;

import java.util.Arrays;
import org.junit.*;
import static org.junit.Assert.*;

/**
 *
 * @author philip
 */
public class SortingTest {

    @Before
    public void before() {
//        System.out.println("SortingTest.before");
    }

    @Test
    public void randomArrayGeneratorTest() {
        int length = 33;
        int[] A = Sorting.randomArrayGenerator(length);

        System.out.println(Arrays.toString(A));
        assertNotNull("Array null", A);
        assertEquals("Array length", length, A.length);

    }

}
