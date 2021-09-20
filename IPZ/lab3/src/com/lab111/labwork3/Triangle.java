package com.lab111.labwork3;

public class Triangle extends Rectangle{
    public void createTriangle(int x1, int y1, int x2, int y2, int x3, int y3){
        System.out.println("\n***I'm starting to build a triangle***");
        create(x1, y1, x2, y2);
        create(x3, y3, x2, y2);
        create(x3, y3, x1, y1);
        System.out.println("--> A triangle with parameters is constructed: " + "((" + x1 + ", " + y1 + "), (" + x2+ ", " + y2 + "), (" + x3+ ", " + y3 +"))\n");

    }
}