/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package DSA.codility;

/**
 *
 * @author philip
 */
public class Codility01 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        long startTime = System.nanoTime();
        
        //new lesson8().runEquiLeader();
        //new lesson9().runMaxSliceSum();
        new lesson9().runMaxDoubleSliceSum();
        
        long endTime = System.nanoTime();

        long duration = (endTime - startTime);
        System.out.println("Function Execution Time="+duration);
    }

}
