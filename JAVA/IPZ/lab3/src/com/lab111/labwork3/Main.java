package com.lab111.labwork3;

public class Main {
    public static void main(String[] args) {
        Line line = new Line();
        line.create(100, 10, 100 ,12);
        Rectangle re = new Rectangle();
        re.createRect(10, 10, 100, 100);
        Triangle triangle = new Triangle();
        triangle.createTriangle(10, 10, 20, 20, 30, 40);
    }
}