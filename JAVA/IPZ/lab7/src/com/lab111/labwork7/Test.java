package com.lab111.labwork7;
/**
 * Test class
 * @author Max Hrytsiuk
 */
public class Test {
    public static void main(String[] args) {
        String s = "String";
        Add add1 = new Add(s +" 1");
        Add add2 = new Add(s +" 2");
        Add add3 = new Add(s +" 3");
        Remove remove = new Remove(s +" 3");
        Edit edit = new Edit(s + " 2");
        Interface inter1 = new Interface(add1);
        Interface inter2 = new Interface(remove);
        Interface inter3 = new Interface(edit);
    }
}
