package com.lab111.labwork2;
/** Class Cl3
 * @author Hrytsiuk Max
 * @version 1.0
 */
public class Cl3 implements If3 {

    /**Method for this class*/
    @Override
    public void meth3() {
        System.out.println("Cl3.meth3() completed!");
    }
    /**Inherited method*/
    @Override
    public void meth2() {
        System.out.println("Cl3.meth2() completed!");
    }

    /**Inherited method*/
    @Override
    public void meth1() {
        System.out.println("Cl3.meth1() completed!");
    }
}
