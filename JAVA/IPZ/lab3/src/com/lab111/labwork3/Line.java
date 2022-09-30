package com.lab111.labwork3;

public class Line  implements Draw{
    @Override
    public void create(int x1, int y1, int x2, int y2) {
        System.out.println("A line with parameters is constructed: " + "((" + x1 + ", " + y1 + "), (" + x2+ ", " + y2 + "))");
    }
}