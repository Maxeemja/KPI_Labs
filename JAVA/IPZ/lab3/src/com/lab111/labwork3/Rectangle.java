package com.lab111.labwork3;

public class Rectangle extends Line {
    public void createRect(int x1, int y1, int x2, int y2){
        System.out.println("\n***I'm starting to build a rectangle***");
        create(x1, y1, x2, y1);
        create(x1, y1, x1, y2);
        create(x1, y2, x2, y2);
        create(x2, y1, x2, y2);
        System.out.println("--> A rectangle with parameters is constructed: " + "((" + x1 + ", " + y1 + "), (" + x2+ ", " + y2 + "))\n");
    }
}
