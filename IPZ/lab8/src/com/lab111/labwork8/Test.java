package com.lab111.labwork8;
import java.util.ArrayList;
import java.util.List;
/**
 *   Main testing class
 *   @author Max Hrytsiuk
 */
public class Test {
    public static void main(String[] args) {
        List<Shape> shapes = new ArrayList<>();
        List<Shape> shapesCopy = new ArrayList<>();

        Circle circle = new Circle();
        circle.x = 10;
        circle.y = 20;
        circle.radius = 15;
        shapes.add(circle);

        Circle anotherCircle = (Circle) circle.clone();
        shapes.add(anotherCircle);

        Rectangle rectangle = new Rectangle();
        rectangle.width = 10;
        rectangle.height = 20;
        shapes.add(rectangle);

        cloneAndCompare(shapes, shapesCopy);
    }

    private static void cloneAndCompare(List<Shape> shapes, List<Shape> shapesCopy) {
        for (Shape shape : shapes) {
            shapesCopy.add(shape.clone());
        }

        for (int i = 0; i < shapes.size(); i++) {
            if (shapes.get(i) != shapesCopy.get(i)) {
                System.out.println(i + ": New figure was created");
                if (shapes.get(i).equals(shapesCopy.get(i))) {
                    System.out.println(i + ": Figures are identical");
                } else {
                    System.out.println(i + ": Figures are different");
                }
            } else {
                System.out.println(i + ": The figure refers to the object");
            }
        }
    }
}
