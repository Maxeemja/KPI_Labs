package com.lab111.labwork4;

/**
 * @author TRudenko
 *
 * Class of an image
 *
 */
public class Image {

    public int height;
    public int width;
    public PointsFactory pf;
    public Points [][] pixels;
    public int randColor = 0;

    /**
     * Constructor that creates an image by corner coordinates and fills it with pixels
     */
    public Image(Coordinates p1, Coordinates p2){
        this.height = p2.y - p1.y + 1;
        this.width = p2.x - p1.x + 1;
        pf = new PointsFactory();

        pixels = new Points[width][];
        for(int i = 0; i < width; i++){
            pixels[i] = new Points[height];
        }

        for(int i = 0; i < width; i++)
            for(int j = 0; j < height; j++){
                randColor = (int)(Math.random()*6);
                pixels[i][j] = pf.addPoint(randColor);
            }

    }

    /**
     * Method that prints an image on the screen pixel by pixel
     */
    public void printImage(){
        for(int i = 0; i < width; i++){
            for(int j = 0; j < height; j++)
                System.out.print(pixels[i][j].color + " ");
            System.out.println("");
        }
    }
}
