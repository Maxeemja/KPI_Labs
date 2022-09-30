package com.lab111.labwork2;

/**
 * 1st class - test class holds void method main that executes all class methods
 * @author Herchuk Volodymyr
 */
public class Test {
    /**
     * main - Invokes at application startup.
     * @param args - Parameters from command line
     */
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Cl1 class1 = new Cl1(); class1.meth1(); class1.meth3();
        Cl2 class2 = new Cl2(); class2.meth2();
        Cl3 class3 = new Cl3(); class3.meth1(); class3.meth3(); class3.meth2();
    }
}
