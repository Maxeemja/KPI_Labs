package com.lab111.labwork4;

/**
 * @author Max Hrytsiuk
 *
 * Class of pixels that implements the Point interface
 *
 */
public class Points implements Point{

    public String color;

    /**
     * Method that draws a pixel
     */
    @Override
    public void draw(Coordinates coord){

    }

    /**
     * Constructor
     */
    public Points(String col){
        this.color = col;
    }
}
