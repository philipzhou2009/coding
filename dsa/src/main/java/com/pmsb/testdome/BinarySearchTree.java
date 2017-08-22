/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.pmsb.testdome;

/**
 *
 * @author philip
 */
public class BinarySearchTree {

    public static boolean contains(Node root, int value) {
//        throw new UnsupportedOperationException("Waiting to be implemented.");

        int rootVal = root.value;
        if (rootVal == value) {
            return true;
        }

        Node left = root.left;

        Node right = root.right;
        if (rootVal < value && right != null) {
            return contains(right, value);
        }
        if (rootVal > value && left != null) {

            return contains(left, value);
        }

        return false;
    }

    public static void run() {
        Node n1 = new Node(1, null, null);
        Node n3 = new Node(3, null, null);
        Node n2 = new Node(2, n1, n3);

        System.out.println(contains(n2, -1));
    }
}

class Node {

    public int value;
    public Node left, right;

    public Node(int value, Node left, Node right) {
        this.value = value;
        this.left = left;
        this.right = right;
    }
}
