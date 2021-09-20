package com.lab111.labwork2;
/** Class Cl1
 * @author Hrytsiuk Max
 * @version 1.0
 */
public class Cl1 implements If1 {
    /**Method for this class*/
    public void meth1() {
        System.out.println("Cl1.meth1() completed!");
    }
    /**Inherited method*/
    public void meth3() {
        System.out.println("Cl1.meth3() completed!");
    }

    @Override
    public void meth2() {

    }
}
