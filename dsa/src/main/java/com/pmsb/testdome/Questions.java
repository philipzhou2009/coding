/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.pmsb.testdome;

import java.util.*;

/**
 *
 * @author philip
 */
public class Questions {

    public static void TrainComposition() {
        TrainComposition tree = new TrainComposition();
        tree.attachWagonFromLeft(7);
        tree.attachWagonFromLeft(13);
        tree.attachWagonFromRight(8);
        tree.attachWagonFromRight(9);
//        System.out.printf("TrainComposition, wagons=%s\n", Arrays.toString(tree.list.toArray()));
        System.out.printf("TrainComposition, wagonsLeft=%s, wagonRight=%s\n", Arrays.toString(tree.listLeft.toArray()), Arrays.toString(tree.listRight.toArray()));
        System.out.println(tree.detachWagonFromRight()); // 7 
        System.out.println(tree.detachWagonFromLeft()); // 13
    }

}

class TrainComposition {

    List<Integer> list = new ArrayList<Integer>();
    List<Integer> listLeft = new ArrayList<Integer>();
    List<Integer> listRight = new ArrayList<Integer>();

    /*
    public void attachWagonFromLeft(int wagonId) {
        list.add(0, wagonId);
    }

    public void attachWagonFromRight(int wagonId) {
        list.add(list.size(), wagonId);

    }

    public int detachWagonFromLeft() {
        return list.remove(0);
    }

    public int detachWagonFromRight() {
        return list.remove(list.size() - 1);
    }
     */
    public void attachWagonFromLeft(int wagonId) {
        listLeft.add(wagonId);

    }

    public void attachWagonFromRight(int wagonId) {
        listRight.add(wagonId);

    }

    public int detachWagonFromLeft() {
        if (listLeft.size() > 0) {
            return listLeft.remove(listLeft.size() - 1);
        }

        return listRight.remove(0);
    }

    public int detachWagonFromRight() {

        if (listRight.size() > 0) {
            return listRight.remove(listRight.size() - 1);
        }

        return listLeft.remove(0);

    }

}
