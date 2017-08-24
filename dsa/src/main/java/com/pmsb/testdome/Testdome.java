/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.pmsb.testdome;

import com.pmsb.Utils;

/**
 *
 * @author philip
 */
public class Testdome {

    public enum Question {
        Palindrome, UserInput, BinarySearchTree, TwoSum, Folders, SortedSearch,
        TrainComposition, Path,
    }

    public static void QFactory(Question q) {

        boolean result = false;
        String sReturn = "";
        switch (q) {
            case Palindrome:
                String s = "Deleveledx";
                result = isPalindrome(s);
                //        Utils.OutputResult("Palindrome", result);
                break;
            case UserInput:
                UserInput();
                break;
            case BinarySearchTree:
                BinarySearchTree.run();
                break;
            case TwoSum:
                findTwoSum();
                break;
            case Folders:
                Folders.run();
                break;
            case SortedSearch:
                countNumbers();
                break;
            case TrainComposition:
                Questions.TrainComposition();
                break;
            case Path:
                Questions.Path();
                break;
        }

    }

    public static boolean isPalindrome(String word) {
        boolean result = true;
        int length = word.length();
        for (int i = 0; i < length; i++) {
            if (Character.toLowerCase(word.charAt(i)) != Character.toLowerCase(word.charAt(length - 1 - i))) {
                result = false;
                break;
            }
        }

        return result;

    }

    public static void UserInput() {
        TextInput input = new NumericInput();
        input.add('1');
        input.add('a');
        input.add('0');
        System.out.println(input.getValue());
    }

    public static class TextInput {

        protected String value = "";

        void add(char c) {
            System.out.println("here");
            this.value += c;
        }

        String getValue() {
            return value;
        }
    }

    public static class NumericInput extends TextInput {

        void add(char c) {
            if (c >= '0' && c <= '9') {
                this.value += c;
            }

        }
    }

    public static void findTwoSum() {
        int[] A = {1, 3, 5, 7, 9};
        int sum = 12;
        int[] result = findTwoSumSolution(A, sum);
        Utils.OutputResult("findTwoSum", result);
    }

    public static int[] findTwoSumSolution(int[] list, int sum) {

        int length = list.length;
        int[] result = new int[2];

        int min = list[0], max = list[0];
        for (int k = 1; k < length; k++) {
            min = list[k] < min ? list[k] : min;
            max = list[k] > max ? list[k] : max;
        }

        int iVal, jVal;
        for (int i = 0; i < length; i++) {
            iVal = list[i];

            if (sum - iVal < min || sum - iVal > max) {
                continue;
            }
            for (int j = i + 1; j < length; j++) {
                if (iVal + list[j] == sum) {
                    result[0] = i;
                    result[1] = j;

                    return result;
                }
            }
        }

        return null;
    }

    public static void countNumbers() {
        int[] A = {1, 2, 3, 5, 7, 9, 11, 12, 13};
        int lessThan = 4;
        int result = countNumbersSolution(A, lessThan);

        Utils.OutputResult("countNumbers", result);
    }

    public static int countNumbersSolution0(int[] sortedArray, int lessThan) {

        int[] A = sortedArray;
        int length = sortedArray.length;
        int result = 0, val, idx, leftCount, len = length;
        /*
        for (int i = 0; i < length; i++) {
            value = sortedArray[i];
            if (value < lessThan) {
                result++;
            } else {
                break;
            }
        }*/

        return result;
    }

    public static int countNumbersSolution(int[] sortedArray, int lessThan) {

        int length = sortedArray.length;
        int result = countNumbersSolutionRecur(sortedArray, 0, length - 1, lessThan);

        return result;
    }

    private static int countNumbersSolutionRecur(int[] A, int left, int right, int lessThan) {

        int length = right - left;

        if (length == 0) {
            return (A[left] < lessThan) ? 1 : 0;
        }

        int mIdx = (left + right) / 2;
        int mid = A[mIdx];
        if (mid < lessThan) {
            return mIdx + 1 - left + countNumbersSolutionRecur(A, mIdx + 1, right, lessThan);
        } else {
            return countNumbersSolutionRecur(A, left, mIdx, lessThan);
        }

    }
}
