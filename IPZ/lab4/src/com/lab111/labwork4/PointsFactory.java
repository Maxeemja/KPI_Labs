package com.lab111.labwork4;

/**
 * @author Max Hrytsia
 *
 * A factory for points, creates one point for each color
 */
public class PointsFactory {

    public final int colorQuantity = 6;
    public final String[] colors = {"Black", "White", "Red", "Green", "Blue", "Pink"};
    public Points[] points = new Points[colorQuantity];

    /**
     * Method that adds a point of a new color
     */
    public Points addPoint(int col){
        if(points[col] == null)
            points[col] = new Points(colors[col]);
        return points[col];
    }
}
