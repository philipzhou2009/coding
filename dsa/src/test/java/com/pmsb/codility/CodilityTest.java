/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.pmsb.codility;

import java.util.concurrent.ThreadLocalRandom;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author philip
 */
public class CodilityTest {

    int iNumber;

    @Before
    public void before() {
        int min = 1, max = 10000;
        iNumber = ThreadLocalRandom.current().nextInt(min, max + 1);

        System.out.println("pmsb::CodilityTest, before, iNumber=" + iNumber);

    }

    @Test
    public void Lesson1Test() {
        int result = Lesson1.solution(iNumber);

        assertTrue("result >= 0", result >= 0);
    }
}
